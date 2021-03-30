from models.domain.checkout import Checkout
from models.schema.schemas import Checkout_List_Pydantic, Checkout_Pydantic
from services.errors import EntityDoesNotExist


async def create_checkout(checkout_create):
    checkout = Checkout(**checkout_create.dict())
    await checkout.save()
    return await Checkout_Pydantic.from_tortoise_orm(checkout)

async def get_all_checkouts():
    checkout_row = await Checkout_List_Pydantic.from_queryset(
        Checkout.all()
    )
    if checkout_row:
        return checkout_row
    raise EntityDoesNotExist()


async def get_checkout(id: int):
    checkout = await Checkout.get_or_none(id=id)
    if checkout:
        return await Checkout_Pydantic.from_tortoise_orm(checkout)
    raise EntityDoesNotExist()
    

async def change_checkout_status(checkout_id, checkout_edit):
    checkout = await Checkout.get_or_none(id=checkout_id)
    checkout.status = checkout_edit['status']
    await checkout.save()
    return await Checkout_Pydantic.from_tortoise_orm(checkout)
