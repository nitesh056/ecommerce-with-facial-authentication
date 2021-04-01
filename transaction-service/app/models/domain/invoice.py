from enum import Enum

from tortoise import fields, models


class TransactionType(str, Enum):
    SALES = "sales"
    PURCHASE = "purchase"


class Invoice(models.Model):
    id = fields.IntField(pk=True)
    transaction_type = fields.CharEnumField(TransactionType, default=TransactionType.PURCHASE)
    grand_total = fields.IntField(pk=False)
