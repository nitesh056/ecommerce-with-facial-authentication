from pydantic import BaseModel, EmailStr
from typing import List

class UserInLogin(BaseModel):
    email: EmailStr
    password: str
    

class UserInfo(BaseModel):
    id: int
    username: str
    name: str
    email: EmailStr
    phone_number: int
    role: str
    status: str
    upload_folder: str
    
class ResponseUser(BaseModel):
    user: UserInfo

class ResponseUserList(BaseModel):
    users: List[UserInfo]

class UserWithToken(BaseModel):
    user: UserInfo
    token: str
    
