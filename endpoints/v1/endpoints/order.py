from fastapi import APIRouter, HTTPException, Query

from schemas import OrderSchema, OrderInDBShema
from crud_async import CRUDOrder


order_router = APIRouter(
    prefix="/order"
)


@order_router.get("/get", response_model=OrderInDBShema, tags=["Order"])
async def get_order(order_id: int = Query(ge=1)):
    order = await CRUDOrder.get(order_id=order_id)
    if order:
        return order
    else:
        raise HTTPException(status_code=404, detail=f"order with id {order_id} not found")

@order_router.get("/all", response_model=list[OrderInDBShema], tags=["Order"])
async def get_all_orders(bot_user_id: int = Query(ge=1)):
    orders = await CRUDOrder.get_all(bot_user_id=bot_user_id)
    return orders


@order_router.post("/add", response_model=OrderInDBShema, tags=["Order"])
async def add_order(order: OrderSchema):
    order = await CRUDOrder.add(order=order)
    if order:
        return order
    else:
        raise HTTPException(status_code=404, detail="order is exist")


@order_router.delete("/del", tags=["Order"])
async def delete_order(order_id: int):
    await CRUDOrder.delete(order_id=order_id)
    raise HTTPException(status_code=200, detail="order was deleted")


@order_router.put("/update", tags=["Order"])
async def update_order(order: OrderInDBShema):
    await CRUDOrder.update(order=order)
    raise HTTPException(status_code=200, detail="order was updated")