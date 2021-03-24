from fastapi import APIRouter, Body, HTTPException, status
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from models.schema.brand import ResponseBrandList, ResponseBrand, ResponseBrandWithAllProducts
from models.schema.schemas import BrandIn_Pydantic, Brand_List_Pydantic, Brand_Pydantic
from resources import strings
from services.brand import (
    create_brand,
    get_all_brands,
    check_brandname_is_taken,
    get_brand
)
from services.errors import EntityDoesNotExist

router = APIRouter()

@router.get("/", name="brand:all")
async def getAll():
    try:
        all_brands = await get_all_brands()
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.PRODUCT_NOT_FOUND_IN_DATABASE,
        )

    return ResponseBrandList(brands=all_brands.dict()['__root__'])


@router.post("/create", name="brand:Create")
async def create(
    brand_create: BrandIn_Pydantic = Body(..., embed=True, alias="brand")
):
    if await check_brandname_is_taken(brand_create.name):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=strings.PRODUCT_NAME_TAKEN,
        )
        
    try:
        brand_obj = await create_brand(brand_create)
        brand = await Brand_Pydantic.from_tortoise_orm(brand_obj)
    except Exception as e:
        HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=strings.ERROR_IN_SAVING_PRODUCT,
        )

    return ResponseBrand(brand=brand)


@router.get("/{brand_name}", name="brand:Get Specific")
async def getSpecific(brand_name):
    try:
        brand = await get_brand(brand_name)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.PRODUCT_NOT_FOUND_IN_DATABASE,
        )

    return ResponseBrandWithAllProducts(brand=brand)