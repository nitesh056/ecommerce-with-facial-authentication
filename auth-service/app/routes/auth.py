from fastapi import APIRouter, Body, Depends, HTTPException, status
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from core import config

from models.domain.user import UserIn_Pydantic, User_Pydantic, User_List_Pydantic, User
from models.schema.user import UserInLogin, UserWithToken, ResponseUserList, ResponseUser
from models.schema.jwt import JWTToken
from resources import strings
from services.jwt import create_access_token_for_user, get_user_id_from_token
import jwt
from services.user import (
    get_user_by_email,
    get_user_by_id,
    check_username_is_taken,
    check_email_is_taken,
    create_user,
    hash_password,
    verify_password,
    get_all_users,
    change_user_role,
    add_upload_folder,
    edit_user
)
from services.errors import EntityDoesNotExist

router = APIRouter()

@router.get("/", name="auth:getAll")
async def getAll():
    try:
        all_users = await get_all_users()
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.USER_NOT_FOUND_IN_DATABASE,
        )

    return ResponseUserList(users=all_users.dict()['__root__'])


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
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=strings.ERROR_IN_SIGNUP,
        )

    token = await create_access_token_for_user(user, "JWT_SECRET")

    return UserWithToken(user=user, token=token)

@router.post("/token", name="auth:token")
async def getUserByToken(
    token: str = Body(..., embed=True, alias="token")
):
    try:
        user_obj = await get_user_by_id(await get_user_id_from_token(token, "JWT_SECRET"))

        user = await User_Pydantic.from_tortoise_orm(user_obj)
    except ValueError as decode_error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="decode_error",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=strings.ERROR_IN_FETCHING_USER,
        )

    return ResponseUser(user=user)


@router.put("/role/{user_id}", name="auth:Change User Role")
async def editRole(
    user_id,
    user_edit = Body(..., embed=True, alias="user")
):
    try:
        user = await change_user_role(user_id, user_edit)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            # detail=strings.ERROR_WHILE_EDITING_PRODUCT,
            detail="error while editing user",
        )
    
    return "role changed"


@router.put("/uploadFolder/{user_name}", name="auth:Change User upload folder")
async def editUploadFolder(
    user_name,
    user_edit=Body(..., embed=True, alias="folderName")
):
    try:
        user = await add_upload_folder(user_name, user_edit)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="error while editing user",
        )

    return "folder name added"

@router.put("/check-email", name="auth:Check Valid Email")
async def checkEmail(
    email=Body(..., embed=True, alias="email")
):
    try:
        user_obj = await get_user_by_email(email=email)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="error while getting email",
        )

    return user_obj.username

@router.put("/check-email/confirm", name="auth:Auth With Email")
async def authWithEmail(
    email=Body(..., embed=True, alias="email")
):
    try:
        user_obj = await get_user_by_email(email=email)
        
        user = await User_Pydantic.from_tortoise_orm(user_obj)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=strings.INCORRECT_LOGIN_INPUT_1,
        )

    token = await create_access_token_for_user(user, "JWT_SECRET")

    return UserWithToken(user=user, token=token)

@router.put("/edit/{user_id}", name="auth:Edit User")
async def editUser(
    user_id,
    user_edit = Body(..., embed=True, alias="user")
):
    if user_edit['password'] == "":
        del user_edit['password']
    else:
        user_edit['password'] = await hash_password(user_edit['password'])
    
    try:
        user = await edit_user(user_id, user_edit)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="error while editing user",
        )
    
    return user

