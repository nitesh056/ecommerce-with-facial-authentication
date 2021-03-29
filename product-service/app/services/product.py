from models.domain.product import Product
from models.schema.schemas import Product_List_Pydantic, Product_Pydantic
from services.errors import EntityDoesNotExist


async def create_product(product_create):
    product = Product(**product_create.dict())
    await product.save()
    return await Product_Pydantic.from_tortoise_orm(product)

async def get_product(id: int):
    product = await Product.get_or_none(id=id).select_related('brand')
    if product:
        return await Product_Pydantic.from_tortoise_orm(product)
    raise EntityDoesNotExist()

async def get_all_products():
    product_row = await Product_List_Pydantic.from_queryset(
        Product.all().select_related('brand')
    )
    if product_row:
        return product_row
    raise EntityDoesNotExist()

async def get_all_active_products():
    product_row = await Product_List_Pydantic.from_queryset(
        Product.filter(status="active").select_related('brand')
    )
    if product_row:
        return product_row
    raise EntityDoesNotExist()

async def check_productname_is_taken(name: str):
    product_row = await Product.get_or_none(name=name).select_related('brand')
    if product_row:
        return True
    return False

async def get_all_gaming_laptop_products():
    product_row = await Product_List_Pydantic.from_queryset(
        Product.filter(is_gaming_laptop=1,status="active").select_related('brand')
    )
    if product_row:
        return product_row
    raise EntityDoesNotExist()

async def get_all_desktop_products():
    product_row = await Product_List_Pydantic.from_queryset(
        Product.filter(is_desktop=1,status="active").select_related('brand')
    )
    if product_row:
        return product_row
    raise EntityDoesNotExist()

async def get_all_new_arrival_products():
    product_row = await Product_List_Pydantic.from_queryset(
        Product.filter(is_new_arrival=1,status="active").select_related('brand')
    )
    if product_row:
        return product_row
    raise EntityDoesNotExist()

async def edit_product(product_id, product_edit):
    product = await Product.get_or_none(id=product_id)
    updated_product = product.update_from_dict(data=product_edit.dict())
    await updated_product.save()
    return await Product_Pydantic.from_tortoise_orm(updated_product)

async def delete_product(product_id):
    product = await Product.get_or_none(id=product_id)
    await product.delete()
