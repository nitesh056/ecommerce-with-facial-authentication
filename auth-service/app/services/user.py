from models.domain.user import User, User_List_Pydantic
from services.errors import EntityDoesNotExist
from passlib.hash import bcrypt

async def get_user_by_email(email: str):
    user_row = await User.get_or_none(email=email)
    if user_row:
        return user_row
    raise EntityDoesNotExist()

async def get_user_by_id(id: int):
    user_row = await User.get_or_none(id=id)
    if user_row:
        return user_row
    raise EntityDoesNotExist()

async def check_username_is_taken(username: str):
    user_row = await User.get_or_none(username=username)
    if user_row:
        return True
    return False

async def check_email_is_taken(email: str):
    user_row = await User.get_or_none(email=email)
    if user_row:
        return True
    return False

async def verify_password(unhashed_password, hashed_password):
    return bcrypt.verify(unhashed_password, hashed_password)

async def hash_password(password):
    return bcrypt.hash(password)

async def create_user(user_create):
    user_obj = User(**user_create.dict())
    await user_obj.save()
    return user_obj

async def edit_user(user_id, user_edit):
    user = await User.get_or_none(id=user_id)
    updated_user = user.update_from_dict(data=user_edit)
    await updated_user.save()
    return "success"

async def get_all_users():
    user_row = await User_List_Pydantic.from_queryset(User.all())
    if user_row:
        return user_row
    raise EntityDoesNotExist()

async def change_user_role(user_id, user_edit):
    user = await User.get_or_none(id=user_id)
    user.role = user_edit['role']
    await user.save()
    return "success"
