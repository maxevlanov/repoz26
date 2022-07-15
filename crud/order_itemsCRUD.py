import sqlite3

conn = sqlite3.connect("db.db")
cur = conn.cursor()

class Order_item CRUD:

    @staticmethod
    def add(order_item:Order_itemSchema) -> None:
        cur.execute("""
        INSERT INTO order_items(order_id, product_id, total);
        """), (order_item.order_id, order_item.product_id, order_item.total)
        conn.commit()

    @staticmethod
    def get(order_id:int) -> Order_itemInDBSchema:
        pass

    @staticmethod
    def get_all() -> list[Order_itemInDBSchema]:
        pass

    @staticmethod
    def update(order_id: int, order_item: Order_itemSchema) -> None:
        pass

    @staticmethod
    def delete(order_id: int) -> None:
        pass