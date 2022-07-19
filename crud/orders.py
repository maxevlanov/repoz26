from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models import Order, create_session
from schemas import OrderScheme, OrderInDBSchema


class CRUDOrder:

    @staticmethod
    @create_session
    def add(order: OrderScheme, session: Session = None) -> OrderInDBSchema | None:
        order = Order(
            **order.dict()
        )
        session.add(order)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(order)
            return OrderInDBSchema(**order.__dict__)

    @staticmethod
    @create_session
    def get(order_id: int, session: Session = None) -> OrderInDBSchema | None:
        order = session.execute(
            select(Order).where(Order.id == order_id)
        )
        order = order.first()
        if order:
            return OrderInDBSchema(**order[0].__dict__)

    @staticmethod
    @create_session
    def get_all(status_id: int = None, session: Session = None) -> list[OrderInDBSchema] | None:
        if status_id:
            orders = session.execute(
                select(order).where(Order.status_id == status_id)
            )
        else:
            orders = session.execute(
                select(Order)
            )
        return [ProductInDBSchema(**order[0].__dict__) for order in orders]

    @staticmethod
    @create_session
    def update(order: OrderInDBSchema, session: Session = None) -> None:
        session.execute(
            update(Order).where(Order.id == order.id).values(
                **order.dict()
            )
        )
        session.commit()

    @staticmethod
    @create_session
    def delete(order_id: int, session: Session = None) -> None:
        session.execute(
            delete(Order).where(order.id == order_id)
        )
        session.commit()