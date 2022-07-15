import sqlite3
from pydantic import BaseModel, Field

class Order_ItemSchema(BaseModel):
    order_id: int = Field(ge=1, default=None)
    product_id: int = Field(default=None)
    total: int = Field(default=None)

class Order_ItemSchemaInDBSchema(Order_ItemSchema):
    id: int = Field(ge=1)

conn = sqlite3.connect("db.db")
cur = conn.cursor()
cur.execute("""
SELECT * FROM order_items;
""")
order_items = []
for order_item in cur.fetchall():
    order_items.append(
        Order_Item(
            id=order_item[0],
            order_id=order_item[1],
            product_id=order_item[2],
            total=order_item[3]
        )
    )
print(order_items)