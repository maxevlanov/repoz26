from fastapi import APIRouter, HTTPException, Query

from schemas import OrderItemSchema, OrderItemInDBShema
from crud_async import CRUDOrderItem


order_item_router = APIRouter(
    prefix="/order_item"
)


@order_item_router.get("/get", response_model=OrderItemInDBShema, tags=["OrderItem"])
async def get_order_item(order_item_id: int = Query(ge=1)):
    order_item = await CRUDOrderItem.get(order_item_id=order_item_id)
    if order_item:
        return order_item
    else:
        raise HTTPException(status_code=404, detail=f"order_item with id {order_item_id} not found")

@order_item_router.get("/all", response_model=list[OrderItemInDBShema], tags=["OrderItem"])
async def get_all_oder_items(order_id: int = Query(ge=1)):
    order_items = await CRUDOrderItem.get_all(order_id=order_id)
    return order_items


@order_item_router.post("/add", responcse_model=OrderItemInDBShema, tags=["OrderItem"])
async def add_order_item(order_item: OrderItemSchema):
    order_item = await CRUDOrderItem.add(order_item=order_item)
    if order_item:
        return order_item
    else:
        raise HTTPException(status_code=404, detail="order_item is exist")


@order_item_router.delete("/del", tags=["OrderItem"])
async def delete_order_item(order_item_id: int):
    await CRUDOrderItem.delete(order_item_id=order_item_id)
    raise HTTPException(status_code=200, detail="order_item was deleted")


@order_item_router.put("/update", tags=["OrderItem"])
async def update_order_item(order_item: OrderItemInDBShema):
    await CRUDOrderItem.update(order_item=order_item)
    raise HTTPException(status_code=200, detail="order_item was updated")