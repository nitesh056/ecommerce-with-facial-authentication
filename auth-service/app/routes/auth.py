from fastapi import APIRouter, Body, Depends, HTTPException, status
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from core import config

from models.domain.user import UserIn_Pydantic, User_Pydantic
from models.schema.user import UserInLogin, UserWithToken
from resources import strings
from services.jwt import create_access_token_for_user
from services.user import (
    get_user_by_email,
    check_username_is_taken,
    check_email_is_taken,
    create_user,
    hash_password,
    verify_password
)
from services.errors import EntityDoesNotExist

router = APIRouter()

@router.get("/", name="auth:home")
async def home():
    return {"home": "page"}

@router.post("/login", name="auth:login")
async def login(
    user_login: UserInLogin = Body(..., embed=True, alias="user")
):
    try:
        user_obj = await get_user_by_email(email=user_login.email)
        
        user = await User_Pydantic.from_tortoise_orm(user_obj)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=strings.INCORRECT_LOGIN_INPUT_1,
        )

    if not await verify_password(user_login.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=strings.INCORRECT_LOGIN_INPUT_2,
        )

    token = await create_access_token_for_user(user, "JWT_SECRET")

    return UserWithToken(user=user, token=token)


@router.post("/register", name="auth:register")
async def register(
    user_create: UserIn_Pydantic = Body(..., embed=True, alias="user")
):
    if await check_username_is_taken(user_create.username):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=strings.USERNAME_TAKEN,
        )

    if await check_email_is_taken(user_create.email):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=strings.EMAIL_TAKEN,
        )
        
    try:
        user_create.password = await hash_password(user_create.password)
        user_obj = await create_user(user_create)
        user = await User_Pydantic.from_tortoise_orm(user_obj)
    except Exception as e:
        HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=strings.ERROR_IN_SIGNUP,
        )

    token = await create_access_token_for_user(user, "JWT_SECRET")

    return UserWithToken(user=user, token=token)
