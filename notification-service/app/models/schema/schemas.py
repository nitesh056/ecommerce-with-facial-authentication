from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from pydantic import BaseModel, EmailStr
from datetime import date, datetime

from models.domain.notification import Notification
from models.domain.generalNotification import GeneralNotification, NotificationSeenStatus


Tortoise.init_models([
    'models.domain.generalNotification',
    'models.domain.notification'
], 'models')


Notification_Pydantic = pydantic_model_creator(Notification, name='Notification')
Notification_List_Pydantic = pydantic_queryset_creator(Notification)

General_Notification_Pydantic = pydantic_model_creator(GeneralNotification, name='General_Notification')
General_Notification_List_Pydantic = pydantic_queryset_creator(GeneralNotification)


class NotificationIn_Pydantic(BaseModel):
    message : str
    redirect_to : str
    recipient : int


class GeneralNotificationIn_Pydantic(BaseModel):
    message: str
    redirect_to: str
    group_type: str

