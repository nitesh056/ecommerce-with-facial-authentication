from models.domain.invoice import Invoice
from models.domain.invoiceItem import InvoiceItem
from models.schema.schemas import Invoice_List_Pydantic, Invoice_Pydantic, Invoice_Item_Pydantic, Invoice_Item_List_Pydantic
from services.errors import EntityDoesNotExist


async def create_invoice(invoice_create):
    invoice = Invoice(**invoice_create.dict())
    await invoice.save()
    return await Invoice_Pydantic.from_tortoise_orm(invoice)

async def get_invoice(user_id: int):
    invoice = await Invoice.get_or_none(user_id=user_id, status='saved')
    if invoice:
        return await Invoice_Pydantic.from_tortoise_orm(invoice)
    raise EntityDoesNotExist()

async def get_all_invoices():
    invoice_row = await Invoice_List_Pydantic.from_queryset(
        Invoice.all()
    )
    if invoice_row:
        return invoice_row
    raise EntityDoesNotExist()

