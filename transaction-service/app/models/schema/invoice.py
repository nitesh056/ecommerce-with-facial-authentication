from pydantic import BaseModel
from typing import List

from models.domain.invoice import Invoice
from models.schema.schemas import InvoiceInfo, InvoiceItemInfo


class InvoiceInfoWithItems(InvoiceInfo):
    invoice_items: InvoiceItemInfo

class ResponseInvoiceWithInvoiceItems(BaseModel):
    invoice: List[InvoiceInfoWithItems]

