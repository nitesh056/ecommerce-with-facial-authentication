from fastapi import APIRouter, Body, HTTPException, status
from starlette.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from models.schema.invoice import InvoiceInfoWithItems, ResponseInvoiceWithInvoiceItems, InvoiceInWithItems
from models.schema.schemas import InvoiceIn_Pydantic
from resources import strings
from services.invoice import (
    create_invoice,
    get_all_invoices,
    get_purchase_invoices,
    get_sales_invoices
)
from services.errors import EntityDoesNotExist

router = APIRouter()


@router.post("/create", name="invoice:Create")
async def create(
    invoice_create = Body(..., embed=True, alias="invoice")
):
    try:
        invoiceInfo = await create_invoice(invoice_create)
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.ERROR_IN_SAVING_INVOICE,
        )
        
    return invoiceInfo


@router.get("/", name="invoice:all invoice")
async def getAll():
    try:
        all_invoices = await get_all_invoices()
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.INVOICE_NOT_FOUND_IN_DATABASE,
        )
    return ResponseInvoiceWithInvoiceItems(invoices=all_invoices.dict()['__root__'])


@router.get("/p", name="invoice:all purchase invoice")
async def getAllPurchase():
    # try:
    all_invoices = await get_purchase_invoices()
    # except:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=strings.INVOICE_NOT_FOUND_IN_DATABASE,
    #     )
    return ResponseInvoiceWithInvoiceItems(invoices=all_invoices.dict()['__root__'])


@router.get("/s", name="invoice:all sales invoice")
async def getAllSales():
    try:
        all_invoices = await get_sales_invoices()
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.INVOICE_NOT_FOUND_IN_DATABASE,
        )
    return ResponseInvoiceWithInvoiceItems(invoices=all_invoices.dict()['__root__'])

