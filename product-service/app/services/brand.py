from models.schema.brand import Brand
from services.errors import EntityDoesNotExist
from models.schema.schemas import BrandIn_Pydantic, Brand_List_Pydantic, Brand_Pydantic

async def create_brand(brand_create):
    brand_obj = Brand(**brand_create.dict())
    await brand_obj.save()
    return brand_obj

async def get_all_brands():
    brand_row = await Brand_List_Pydantic.from_queryset(Brand.all())
    if brand_row:
        return brand_row
    raise EntityDoesNotExist()

async def check_brandname_is_taken(name: str):
    brand_row = await Brand.get_or_none(name=name)
    if brand_row:
        return True
    return False

async def get_brand(brand_name):
    brand = await Brand.get_or_none(name=brand_name).prefetch_related('products')
    if brand:
        return await Brand_Pydantic.from_tortoise_orm(brand)
    raise EntityDoesNotExist()
