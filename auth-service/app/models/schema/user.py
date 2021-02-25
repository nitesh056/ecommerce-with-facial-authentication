from pydantic import BaseModel, EmailStr


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
    

class UserWithToken(BaseModel):
    user: UserInfo
    token: str
    