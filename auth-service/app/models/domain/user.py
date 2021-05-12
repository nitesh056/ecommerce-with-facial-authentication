from enum import Enum

from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from tortoise import fields, models

class Status(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class Role(str, Enum):
    ADMIN = "admin"
    STAFF = "staff"
    USER = "user"

class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    name = fields.CharField(50)
    email = fields.CharField(50, unique=True)
    password = fields.CharField(128)
    phone_number = fields.BigIntField(pk=False)
    role = fields.CharEnumField(Role, default=Role.USER)
    status = fields.CharEnumField(Status, default=Status.INACTIVE)
    upload_folder = fields.CharField(50, null=True, default=None)


Tortoise.init_models([
    'models.domain.user',
], 'models')

User_Pydantic = pydantic_model_creator(User, name='User')
User_List_Pydantic = pydantic_queryset_creator(User)
UserIn_Pydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)
