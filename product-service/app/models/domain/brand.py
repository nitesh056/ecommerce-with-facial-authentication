from enum import Enum

from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from tortoise import fields, models

class Status(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class Brand(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(255, unique=True)
    status = fields.CharEnumField(Status, default=Status.ACTIVE)
    # product = fields.ForeignKeyField('models.Product', related_name='products', to_field="brand_id")
    # image = fields.CharField(255)
    