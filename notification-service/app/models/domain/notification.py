from tortoise import fields, models


class Notification(models.Model):
    id = fields.IntField(pk=True)
    message = fields.CharField(255)
    redirect_to = fields.CharField(255)
    recipient = fields.IntField(pk=False)
    seen = fields.BooleanField(pk=False, default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
