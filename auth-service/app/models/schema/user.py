from pydantic import BaseModel, EmailStr
from typing import List


class UserInLogin(BaseModel):
    email: EmailStr
    password: str
    

class UserInfo(BaseModel):
    username: str
    name: str
    email: EmailStr
    phone_number: int
    role_id: int
    status: str
    

class ResponseUserList(BaseModel):
    users: List[UserInfo]


class UserWithToken(BaseModel):
    user: UserInfo
    token: str
    