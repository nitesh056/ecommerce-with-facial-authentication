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

    thisone = await create_invoice(invoice_create)
    # await create_invoice({
    #     transaction_type: invoice_create.transaction_type,
    #     grand_total: invoice_create.grand_total
    # })
    return thisone
    # return InvoiceIn_Pydantic(**invoice_create.dict())
    # invoice = await create_invoice(invoice_create.)
    # try:
    # except Exception as e:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail=strings.ERROR_IN_SAVING_CART,
    #     )

    # return ResponseInvoice(invoice=invoice.dict())


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
    try:
        all_invoices = await get_purchase_invoices()
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.INVOICE_NOT_FOUND_IN_DATABASE,
        )
    return ResponseInvoiceWithInvoiceItems(invoices=all_invoices.dict()['__root__'])


@router.get("/s", name="invoice:all sales invoice")
async def getAllPurchase():
    try:
        all_invoices = await get_sales_invoices()
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=strings.INVOICE_NOT_FOUND_IN_DATABASE,
        )
    return ResponseInvoiceWithInvoiceItems(invoices=all_invoices.dict()['__root__'])


# @router.post("/add-invoice-item", name="invoice:Add Item In Invoice")
# async def addItemInInvoice(addInvoiceItemReqest: AddInvoiceItemRequest):
#     try:
#         invoice = await get_specific_user_invoice(addInvoiceItemReqest.user_id)
#     except:
#         invoice = await create_invoice(InvoiceIn_Pydantic(
#             user_id=addInvoiceItemReqest.user_id,
#             grand_total=0,
#             status='saved'))

#     invoiceItem = await edit_quantity_in_invoice(invoice.id, addInvoiceItemReqest.product_id, 1)

#     invoice = await edit_invoice(invoice.id, invoice.grand_total + invoiceItem.product.current_price)

#     return ResponseInvoiceWithInvoiceItems(**invoice.dict())


# @router.post("/remove-invoice-item", name="invoice:Remove Item In Invoice")
# async def removeItemInInvoice(addInvoiceItemReqest: AddInvoiceItemRequest):
#     try:
#         invoice = await get_specific_user_invoice(addInvoiceItemReqest.user_id)
#     except:
#         invoice = await create_invoice(InvoiceIn_Pydantic(
#             user_id=addInvoiceItemReqest.user_id,
#             grand_total=0,
#             status='saved'))

#     invoiceItem = await edit_quantity_in_invoice(invoice.id, addInvoiceItemReqest.product_id, -1)

#     invoice = await edit_invoice(invoice.id, invoiceItem.quantity * invoiceItem.product.current_price)

#     return ResponseInvoiceWithInvoiceItems(**invoice.dict())
    

# @router.post("/checkout", name="invoice:Add Checkout")
# async def checkout(
#     checkout_create: CheckoutIn_Pydantic = Body(..., embed=True, alias="checkout")
# ):
#     try:
#         checkout = await create_checkout(checkout_create)

#         invoice = await edit_invoice_status(checkout_create.invoice_id, 'awaiting')
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail=strings.ERROR_IN_SAVING_CART,
#         )

#     return ResponseCheckout(checkout=checkout.dict())


# @router.get("/checkout", name="invoice:Get Checkout")
# async def getPendingCheckouts():
#     try:
#         checkouts = await get_all_checkouts()
#         print(checkouts)
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail=strings.ERROR_IN_SAVING_CART,
#         )

#     return ResponseCheckoutList(checkouts=checkouts.dict()['__root__'])


# @router.get("/checkout/{checkout_id}", name="invoice:Get Specific Checkout")
# async def getPendingCheckouts(checkout_id):
#     try:
#         checkout = await get_checkout(checkout_id)
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail=strings.ERROR_IN_SAVING_CART,
#         )

#     return CheckoutWithInvoice(**checkout.dict())


# @router.put("/checkout/{checkout_id}", name="invoice:Change Checkout Status")
# async def edit(
#     checkout_id,
#     checkout_edit = Body(..., embed=True, alias="checkout")
# ):
#     try:
#         checkout = await change_checkout_status(checkout_id, checkout_edit)
#     except:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             # detail=strings.ERROR_WHILE_EDITING_PRODUCT,
#             detail="error while editing checkout",
#         )

#     return "success"


# @router.get("/{user_id}", name="invoice:Get Specific")
# async def getSpecific(user_id):
#     try:
#         invoice = await get_invoice(user_id)
#     except:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=strings.CART_NOT_FOUND_IN_DATABASE,
#         )

#     return ResponseInvoiceWithInvoiceItems(**invoice.dict())
