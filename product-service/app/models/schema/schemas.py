from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from pydantic import BaseModel

from models.domain.brand import Brand
from models.domain.product import Product
from models.domain.cart import Cart
from models.domain.cartItem import CartItem


Tortoise.init_models([
    'models.domain.brand',
    'models.domain.product',
    'models.domain.cart',
    'models.domain.cartItem',
    'models.domain.checkout'
], 'models')

Product_Pydantic = pydantic_model_creator(Product, name='Product')
Product_List_Pydantic = pydantic_queryset_creator(Product)
ProductIn_Pydantic = pydantic_model_creator(Product, name='ProductIn', exclude_readonly=True)

Brand_Pydantic = pydantic_model_creator(Brand, name='Brand')
Brand_List_Pydantic = pydantic_queryset_creator(Brand)
BrandIn_Pydantic = pydantic_model_creator(Brand, name='BrandIn', exclude_readonly=True)

Cart_Pydantic = pydantic_model_creator(Cart, name='Cart')
Cart_List_Pydantic = pydantic_queryset_creator(Cart)
CartIn_Pydantic = pydantic_model_creator(Cart, name='CartIn', exclude_readonly=True)

Cart_Item_Pydantic = pydantic_model_creator(CartItem, name='CartItem')
Cart_Item_List_Pydantic = pydantic_queryset_creator(CartItem)


class BrandInfo(BaseModel):
    id: int
    name: str
    status: str

class ProductInfo(BaseModel):
    id: int
    name: str
    old_price: int
    current_price: int
    qty: int
    image: str
    short_description: str
    description: str
    features: str
    is_gaming_laptop: int
    is_gaming_laptop: int
    is_desktop: int
    is_new_arrival: int
    status: str

class CartInfo(BaseModel):
    id: int
    user_id: int
    grand_total: int
    status: str


class CartItemInfo(BaseModel):
    id: int
    quantity: int
