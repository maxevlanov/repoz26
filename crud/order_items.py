from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models import OrderItem, create_session
from schemas import OrderItemScheme, OrderItemInDBSchema


class CRUDOrderItem:

    @staticmethod
    @create_session
    def add(order_item: OrderItemScheme, session: Session = None) -> OrderItemInDBSchema | None:
        order_item = OrderItem(
            **order_item.dict()
        )
        session.add(order_item)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(order_item)
            return OrderItemInDBSchema(**order_item.__dict__)

    @staticmethod
    @create_session
    def get(order_item_id: int, session: Session = None) -> OrderItemInDBSchema | None:
        order_item = session.execute(
            select(order_item).where(OrderItem.id == order_item_id)
        )
        order_item = order_item.first()
        if order_item:
            return OrderItemInDBSchema(**order_item[0].__dict__)

    @staticmethod
    @create_session
    def get_all(order_id: int = None, session: Session = None) -> list[OrderItemInDBSchema] | None:
        if order_id:
            order_items = session.execute(
                select(order_item).where(order_item.order_id == order_id)
            )
        else:
            order_items = session.execute(
                select(Order_item)
            )
        return [OrderItemInDBSchema(**order_item[0].__dict__) for order_item in order_items]

    @staticmethod
    @create_session
    def update(order_item: OrderItemInDBSchema, session: Session = None) -> None:
        session.execute(
            update(OrderItem).where(OrderItem.id == order_item.id).values(
                **order_item.dict()
            )
        )
        session.commit()

    @staticmethod
    @create_session
    def delete(order_item_id: int, session: Session = None) -> None:
        session.execute(
            delete(OrderItem).where(OrderItem.id == order_item_id)
        )
        session.commit()