from fastapi import APIRouter, Body, HTTPException, status
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from models.schema.cart import ResponseCartList, ResponseCart, AddCartItemRequest
from models.schema.schemas import CartIn_Pydantic, Cart_Pydantic
from resources import strings
from services.cart import (
    create_cart,
    get_cart,
    get_all_carts,
    get_specific_user_cart,
    edit_cart,
    edit_quantity_in_cart
)
from services.errors import EntityDoesNotExist

router = APIRouter()


@router.get("/all", name="cart:all")
async def getAll():
    try:
        all_carts = await get_all_carts()
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.CART_NOT_FOUND_IN_DATABASE,
        )
    return ResponseCartList(carts=all_carts.dict()['__root__'])


@router.post("/create", name="cart:Create")
async def create(
    cart_create: CartIn_Pydantic = Body(..., embed=True, alias="cart")
):      
    try:
        cart = await create_cart(cart_create)
    except Exception as e:
        HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=strings.ERROR_IN_SAVING_CART,
        )

    return ResponseCart(cart=cart.dict())


@router.get("/{cart_id}", name="cart:Get Specific")
async def getSpecific(cart_id):
    try:
        cart = await get_cart(cart_id)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.CART_NOT_FOUND_IN_DATABASE,
        )

    return ResponseCart(cart=cart.dict())


@router.post("/add-cart-item", name="cart:Add Item In Cart")
async def addItemInCart(addCartItemReqest: AddCartItemRequest):
    try:
        cart = await get_specific_user_cart(addCartItemReqest.user_id)
    except:
        cart = await create_cart(CartIn_Pydantic(
            user_id=addCartItemReqest.user_id,
            grand_total=0,
            status='saved'))

    cartItem = await edit_quantity_in_cart(cart.id, addCartItemReqest.product_id, 1)

    cart = await edit_cart(cart.id, cart.grand_total + cartItem.product.current_price)

    return ResponseCart(cart=cart.dict())


@router.post("/remove-cart-item", name="cart:Remove Item In Cart")
async def removeItemInCart(addCartItemReqest: AddCartItemRequest):
    try:
        cart = await get_specific_user_cart(addCartItemReqest.user_id)
    except:
        cart = await create_cart(CartIn_Pydantic(
            user_id=addCartItemReqest.user_id,
            grand_total=0,
            status='saved'))

    cartItem = await edit_quantity_in_cart(cart.id, addCartItemReqest.product_id, -1)

    cart = await edit_cart(cart.id, cartItem.quantity * cartItem.product.current_price)

    return ResponseCart(cart=cart.dict())
