from pydantic import BaseModel
from typing import List

from models.domain.cart import Cart
from models.schema.schemas import BrandInfo, ProductInfo, CartInfo, CheckoutInfo


class CartItemInfo(BaseModel):
    id: int
    quantity: int
    product: ProductInfo

class ResponseCartList(BaseModel):
    carts: List[CartInfo]

class ResponseCart(BaseModel):
    cart: CartInfo

class ResponseCartWithCartItems(CartInfo):
    cart_items: List[CartItemInfo]

class AddCartItemRequest(BaseModel):
    user_id: int
    product_id: int


class ResponseCheckout(BaseModel):
    checkout: CheckoutInfo
