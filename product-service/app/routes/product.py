from fastapi import APIRouter, Body, HTTPException, status
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from models.schema.product import ResponseProductList, ResponseProduct, ProductInfoWithBrand, ProductInfo, ResponseProductWithBrand
from models.schema.schemas import ProductIn_Pydantic, Product_Pydantic
from resources import strings
from services.product import (
    create_product,
    get_product,
    get_all_products,
    get_all_active_products,
    check_productname_is_taken,
    get_all_gaming_laptop_products,
    get_all_desktop_products,
    get_all_new_arrival_products
)
from services.errors import EntityDoesNotExist

router = APIRouter()


@router.get("/all", name="product:all")
async def getAll():
    try:
        all_products = await get_all_products()
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.PRODUCT_NOT_FOUND_IN_DATABASE,
        )
    return ResponseProductList(products=all_products.dict()['__root__'])


@router.get("/", name="product:Active-Product")
async def getAllActiveProducts():
    try:
        all_products = await get_all_active_products()
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.PRODUCT_NOT_FOUND_IN_DATABASE,
        )

    return ResponseProductList(products=all_products.dict()['__root__'])


@router.post("/create", name="product:Create")
async def create(
    product_create: ProductIn_Pydantic = Body(..., embed=True, alias="product")
):
    if await check_productname_is_taken(product_create.name):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=strings.PRODUCT_NAME_TAKEN,
        )
        
    try:
        product = await create_product(product_create)
    except Exception as e:
        HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=strings.ERROR_IN_SAVING_PRODUCT,
        )

    return ResponseProductWithBrand(product=product.dict())


@router.get("/gaming-laptop", name="product:Gaming Laptop")
async def getAllGamingLaptop():
    try:
        all_products = await get_all_gaming_laptop_products()
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.PRODUCT_NOT_FOUND_IN_DATABASE,
        )

    return ResponseProductList(products=all_products.dict()['__root__'])

@router.get("/desktop", name="product:Desktop")
async def getAllDesktop():
    try:
        all_products = await get_all_desktop_products()
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.PRODUCT_NOT_FOUND_IN_DATABASE,
        )

    return ResponseProductList(products=all_products.dict()['__root__'])


@router.get("/new-arrival", name="product:New Arrival")
async def getAllNewArrival():
    try:
        all_products = await get_all_new_arrival_products()
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.PRODUCT_NOT_FOUND_IN_DATABASE,
        )

    return ResponseProductList(products=all_products.dict()['__root__'])


@router.get("/{product_id}", name="product:Get Specific")
async def getSpecific(product_id):
    try:
        product = await get_product(product_id)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.PRODUCT_NOT_FOUND_IN_DATABASE,
        )

    return ProductInfoWithBrand(**product.dict())