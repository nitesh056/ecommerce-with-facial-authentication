from pydantic import BaseModel
from typing import List

from models.domain.invoice import Invoice
from models.schema.schemas import InvoiceInfo, InvoiceItemInfo, InvoiceIn_Pydantic, Invoice_ItemIn_Pydantic


class InvoiceInfoWithItems(InvoiceInfo):
    invoice_items: List[InvoiceItemInfo]

class ResponseInvoiceWithInvoiceItems(BaseModel):
    invoices: List[InvoiceInfoWithItems]

class InvoiceInWithItems(InvoiceIn_Pydantic):
    invoice_items: List[Invoice_ItemIn_Pydantic]