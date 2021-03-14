from enum import Enum

from tortoise import fields, models

class Status(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class Product(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(255, unique=True)
    old_price = fields.IntField(pk=False)
    current_price = fields.IntField(pk=False)
    qty = fields.IntField(pk=False)
    image = fields.CharField(255)
    short_description = fields.TextField()
    description = fields.TextField()
    features = fields.TextField()
    is_gaming_laptop = fields.SmallIntField(pk=False)
    is_desktop = fields.SmallIntField(pk=False)
    is_new_arrival = fields.SmallIntField(pk=False)
    brand = fields.ForeignKeyField('models.Brand', related_name='products')
    status = fields.CharEnumField(Status, default=Status.ACTIVE)

    class Meta:
        default_related_name = 'products'
