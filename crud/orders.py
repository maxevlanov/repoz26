import sqlite3

conn = sqlite3.connect("db.db")
cur = conn.cursor()

class Order CRUD:

    @staticmethod
    def add(order:CategorySchema) -> None:
        cur.execute("""
        INSERT INTO orders(bot_user_id, date_created, status_id, invoice_id);
        """), (order.bot_user_id, order.date_created, order.status_id, order.invoice_id)
        conn.commit()

    @staticmethod
    def get(order_id:int) -> OrderInDBSchema:
        pass

    @staticmethod
    def get_all() -> list[OrderInDBSchema]:
        pass

    @staticmethod
    def update(order_id: int, order: OrderSchema) -> None:
        pass

    @staticmethod
    def delete(order_id: int) -> None:
        pass