from pydantic import BaseModel
from typing import List

from models.domain.product import Product
from models.schema.schemas import BrandInfo, ProductInfo


class ProductInfoWithBrand(ProductInfo):
    brand: BrandInfo

# class ProductListWithBrand(BaseModel):
#     products: List[ProductInfoWithBrand]

class ResponseProductWithBrand(BaseModel):
    product: ProductInfoWithBrand

class ResponseProductList(BaseModel):
    products: List[ProductInfoWithBrand]

class ResponseProduct(BaseModel):
    product: ProductInfo