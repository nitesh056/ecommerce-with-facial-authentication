from fastapi import APIRouter, Body, HTTPException, status
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from models.schema.notification import ResponseNotificatonList, ResponseGeneralNotificatonList
from models.schema.schemas import NotificationIn_Pydantic, GeneralNotificationIn_Pydantic
from resources import strings
from services.notification import (
    create_notification,
    create_general_notification,
    get_all_notifications,
    get_all_general_notifications
)
from services.errors import EntityDoesNotExist

router = APIRouter()


@router.post("/n/create", name="notification:Create")
async def create(
    notification_create: NotificationIn_Pydantic = Body(..., embed=True, alias="notification")
):
    try:
        notification = await create_notification(notification_create)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=strings.ERROR_IN_SAVING_NOTIFICATION,
        )
    
    return notification

@router.post("/g/create", name="notification:Create General")
async def create(
    notification_create: GeneralNotificationIn_Pydantic = Body(..., embed=True, alias="notification")
):
    try:
        notification = await create_general_notification(notification_create)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=strings.ERROR_IN_SAVING_NOTIFICATION,
        )
    
    return notification


@router.get("/n/{user_id}", name="notification:get all notifications")
async def getAllNotification(user_id):
    try:
        all_notifications = await get_all_notifications(user_id)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.NOTIFICATION_NOT_FOUND_IN_DATABASE,
        )

    # return all_notifications
    return ResponseNotificatonList(notifications=all_notifications.dict()['__root__'])


@router.get("/g/{role}", name="notification:get all general notifications")
async def getAllGeneralNotification(role):
    try:
        all_general_notifications = await get_all_general_notifications(role)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.NOTIFICATION_NOT_FOUND_IN_DATABASE,
        )

    return ResponseGeneralNotificatonList(notifications=all_general_notifications.dict()['__root__'])

