from models.domain.checkout import Checkout
from models.schema.schemas import Checkout_List_Pydantic, Checkout_Pydantic
from services.errors import EntityDoesNotExist


async def create_checkout(checkout_create):
    checkout = Checkout(**checkout_create.dict())
    await checkout.save()
    return await Checkout_Pydantic.from_tortoise_orm(checkout)


# async def get_checkout(user_id: int):
#     checkout = await Checkout.get_or_none(user_id=user_id, status='saved').prefetch_related('checkout_items')
#     if checkout:
#         return await Checkout_Pydantic.from_tortoise_orm(checkout)
#     raise EntityDoesNotExist()
