from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from pydantic import BaseModel, EmailStr

from models.domain.invoice import Invoice
from models.domain.invoiceItem import InvoiceItem


Tortoise.init_models([
    'models.domain.invoice',
    'models.domain.invoiceItem'
], 'models')


Invoice_Pydantic = pydantic_model_creator(Invoice, name='Invoice')
Invoice_List_Pydantic = pydantic_queryset_creator(Invoice)
InvoiceIn_Pydantic = pydantic_model_creator(Invoice, name='InvoiceIn', exclude_readonly=True)

Invoice_Item_Pydantic = pydantic_model_creator(InvoiceItem, name='InvoiceItem')
Invoice_Item_List_Pydantic = pydantic_queryset_creator(InvoiceItem)


class InvoiceInfo(BaseModel):
    id: int
    transaction_type: str
    grand_total: int

class InvoiceItemInfo(BaseModel):
    id: int
    product_id: int
    quantity: int
    rate: int
