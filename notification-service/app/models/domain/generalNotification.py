from enum import Enum

from tortoise import fields, models


class GroupType(str, Enum):
    ADMIN = "admin"
    CUSTOMER = "customer"


class GeneralNotification(models.Model):
    id = fields.IntField(pk=True)
    message = fields.CharField(255)
    redirect_to = fields.CharField(255)
    group_type = fields.CharEnumField(GroupType, default=GroupType.ADMIN)
    created_at = fields.DatetimeField(auto_now_add=True)


class NotificationSeenStatus(models.Model):
    id = fields.IntField(pk=True)
    notification = fields.ForeignKeyField('models.GeneralNotification', related_name='notification_user_status')
    seen_by = fields.IntField(pk=False)

