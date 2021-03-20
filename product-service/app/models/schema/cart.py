from pydantic import BaseModel
from typing import List

from models.domain.cart import Cart
from models.schema.schemas import BrandInfo, ProductInfo, CartInfo, CartItemInfo


# class CartInfoWithBrand(CartInfo):
#     brand: BrandInfo

# class CartInfoWithBrand(CartInfo):
#     brand: BrandInfo

# class CartListWithBrand(BaseModel):
#     carts: List[CartInfoWithBrand]

# class ResponseCartWithBrand(BaseModel):
#     cart: CartInfoWithBrand

class ResponseCartList(BaseModel):
    carts: List[CartInfo]

class ResponseCart(BaseModel):
    cart: CartInfo

class AddCartItemRequest(BaseModel):
    user_id: int
    product_id: int