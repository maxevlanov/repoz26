from fastapi import APIRouter, HTTPException, Query

from schemas import InvoiceSchema, InvoiceInDBShema
from crud_async import CRUDInvoice


invoice_router = APIRouter(
    prefix="/invoice"
)


@invoice_router.get("/get", response_model=InvoiceInDBShema, tags=["Invoice"])
async def get_invoice(invoice_id: int = Query(ge=1)):
    invoice = await CRUDInvoice.get(invoice_id=invoice_id)
    if invoice:
        return invoice
    else:
        raise HTTPException(status_code=404, detail=f"invoice with id {invoice_id} not found")

@invoice_router.get("/all", response_model=list[InvoiceInDBShema], tags=["Invoice"])
async def get_all_invoices(bot_user_id: int = Query(ge=1)):
    invoices = await CRUDInvoice.get_all(bot_user_id=bot_user_id)
    return invoices


@invoice_router.post("/add", responcse_model=InvoiceInDBShema, tags=["Invoice"])
async def add_invoice(invoice: InvoiceSchema):
    invoice = await CRUDInvoice.add(invoice=invoice)
    if invoice:
        return invoice
    else:
        raise HTTPException(status_code=404, detail="invoice is exist")


@invoice_router.delete("/del", tags=["Invoice"])
async def delete_invoice(invoice_id: int):
    await CRUDInvoice.delete(invoice_id=invoice_id)
    raise HTTPException(status_code=200, detail="invoice was deleted")


@invoice_router.put("/update", tags=["Invoice"])
async def update_invoice(invoice: InvoiceInDBShema):
    await CRUDInvoice.update(invoice=invoice)
    raise HTTPException(status_code=200, detail="invoice was updated")