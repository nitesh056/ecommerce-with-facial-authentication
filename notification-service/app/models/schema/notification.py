from pydantic import BaseModel
from typing import List

from models.schema.schemas import Notification_Pydantic, General_Notification_Pydantic


class ResponseNotificatonList(BaseModel):
    notifications: List[Notification_Pydantic]


class ResponseGeneralNotificatonList(BaseModel):
    notifications: List[General_Notification_Pydantic]
