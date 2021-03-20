from enum import Enum

from tortoise import fields, models


class CheckoutStatus(str, Enum):
    PENDING = "pending"
    CANCELED = "canceled"
    APPROVED = "approved"


class Checkout(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(255)
    email = fields.CharField(255)
    address = fields.CharField(255)
    phone_no = fields.CharField(255)
    cart = fields.ForeignKeyField('models.Cart', related_name='checkout')
    status = fields.CharEnumField(CheckoutStatus, default=CheckoutStatus.PENDING)
    remarks = fields.CharField(255)
