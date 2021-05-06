from models.domain.notification import Notification
from models.domain.generalNotification import GeneralNotification, NotificationSeenStatus
from models.schema.schemas import Notification_List_Pydantic, Notification_Pydantic, General_Notification_Pydantic, General_Notification_List_Pydantic
from services.errors import EntityDoesNotExist


async def create_notification(notification_create):
    notification = Notification(**notification_create.dict())
    await notification.save()
    return await Notification_Pydantic.from_tortoise_orm(notification)


async def create_general_notification(notification_create):
    notification = GeneralNotification(**notification_create.dict())
    await notification.save()
    return await General_Notification_Pydantic.from_tortoise_orm(notification)


async def get_all_notifications(user_id):
    notification_row = await Notification_List_Pydantic.from_queryset(
        Notification.filter(recipient=user_id)
    )
    if notification_row:
        return notification_row
    raise EntityDoesNotExist()


async def get_all_general_notifications(role):
    general_notification_row = await General_Notification_List_Pydantic.from_queryset(
        GeneralNotification.filter(group_type=role)
    )
    if general_notification_row:
        return general_notification_row
    raise EntityDoesNotExist()

