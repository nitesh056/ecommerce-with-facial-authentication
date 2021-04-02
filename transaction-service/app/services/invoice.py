from models.domain.invoice import Invoice
from models.domain.invoiceItem import InvoiceItem
from models.schema.schemas import Invoice_List_Pydantic, Invoice_Pydantic, Invoice_Item_Pydantic, Invoice_Item_List_Pydantic
from models.schema.invoice import InvoiceInWithItems
from services.errors import EntityDoesNotExist


async def create_invoice(invoice_create):
    invoice_copy = dict(invoice_create)
    del invoice_copy['invoice_items']
    invoice = await Invoice.create(**invoice_copy)

    def insertInvoiceInInvoiceItem(item):
        item['invoice'] = invoice
        itemObj = InvoiceItem(**item)
        return itemObj

    await InvoiceItem.bulk_create(list(map(insertInvoiceInInvoiceItem, invoice_create['invoice_items'])))

    return InvoiceInWithItems(
        **invoice_copy,
        invoice_items=invoice_create['invoice_items']
    )
    

# async def get_invoice(user_id: int):
#     invoice = await Invoice.get_or_none(user_id=user_id, status='saved')
#     if invoice:
#         return await Invoice_Pydantic.from_tortoise_orm(invoice)
#     raise EntityDoesNotExist()

async def get_all_invoices():
    invoice_row = await Invoice_List_Pydantic.from_queryset(Invoice.all())
    if invoice_row:
        return invoice_row
    raise EntityDoesNotExist()

async def get_purchase_invoices():
    invoice_row = await Invoice_List_Pydantic.from_queryset(
        Invoice.filter(transaction_type="purchase")
    )
    if invoice_row:
        return invoice_row
    raise EntityDoesNotExist()

async def get_sales_invoices():
    invoice_row = await Invoice_List_Pydantic.from_queryset(
        Invoice.filter(transaction_type="sales")
    )
    if invoice_row:
        return invoice_row
    raise EntityDoesNotExist()