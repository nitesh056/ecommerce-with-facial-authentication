from models.domain.cart import Cart
from models.domain.cartItem import CartItem
from models.schema.schemas import Cart_List_Pydantic, Cart_Pydantic, Cart_Item_Pydantic, Cart_Item_List_Pydantic
from services.errors import EntityDoesNotExist


async def create_cart(cart_create):
    cart = Cart(**cart_create.dict())
    await cart.save()
    return await Cart_Pydantic.from_tortoise_orm(cart)

async def get_cart(id: int):
    cart = await Cart.get_or_none(id=id)
    if cart:
        return await Cart_Pydantic.from_tortoise_orm(cart)
    raise EntityDoesNotExist()

async def get_all_carts():
    cart_row = await Cart_List_Pydantic.from_queryset(
        Cart.all()
    )
    if cart_row:
        return cart_row
    raise EntityDoesNotExist()

async def get_specific_user_cart(user_id):
    cart_row = await Cart.get_or_none(user_id=user_id, status='saved')
    if cart_row:
        return await Cart_Pydantic.from_tortoise_orm(cart_row)
    raise EntityDoesNotExist()

async def edit_cart(id, grand_total):
    to_update_row = await Cart.get_or_none(id=id)
    if to_update_row:
        to_update_row.grand_total = grand_total
        await to_update_row.save()
        return await Cart_Pydantic.from_tortoise_orm(to_update_row)
    raise EntityDoesNotExist()

async def edit_quantity_in_cart(cart_id, product_id, quantity):
    cart_item_row = await CartItem.get_or_none(cart_id=cart_id, product_id=product_id)
    if cart_item_row:
        cart_item_row.quantity = cart_item_row.quantity + quantity
    else:
        cart_item_row = CartItem(quantity=1, cart_id=cart_id, product_id=product_id)
    # if cart_item_row.quantity <= 0:
    #     await cart_item_row.delete()
    #     return ""
    # else:
    await cart_item_row.save()
    return await Cart_Item_Pydantic.from_tortoise_orm(cart_item_row)


