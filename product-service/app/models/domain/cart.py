from enum import Enum

from tortoise import fields, models


class CartStatus(str, Enum):
    SAVED = "saved"
    AWAITING = "awaiting"


class Cart(models.Model):
    id = fields.IntField(pk=True)
    user_id = fields.IntField(pk=False)
    grand_total = fields.IntField(pk=False)
    status = fields.CharEnumField(CartStatus, default=CartStatus.SAVED)
