from pydantic import BaseModel
from typing import List

from models.domain.brand import Brand
from models.schema.schemas import BrandInfo, ProductInfo


class BrandWithAllProducts(BrandInfo):
    products: List[ProductInfo]

class ResponseBrandList(BaseModel):
    brands: List[BrandInfo]

class ResponseBrand(BaseModel):
    brand: BrandInfo

class ResponseBrandWithAllProducts(BaseModel):
    brand: BrandWithAllProducts