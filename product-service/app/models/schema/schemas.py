from tortoise import Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator
from pydantic import BaseModel

from models.domain.brand import Brand
from models.domain.product import Product


Tortoise.init_models(['models.domain.brand', 'models.domain.product'], 'models')

Product_Pydantic = pydantic_model_creator(Product, name='Product')
Product_List_Pydantic = pydantic_queryset_creator(Product)
ProductIn_Pydantic = pydantic_model_creator(Product, name='ProductIn', exclude_readonly=True)

Brand_Pydantic = pydantic_model_creator(Brand, name='Brand')
Brand_List_Pydantic = pydantic_queryset_creator(Brand)
BrandIn_Pydantic = pydantic_model_creator(Brand, name='BrandIn', exclude_readonly=True)

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