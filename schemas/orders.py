import sqlite3
from pydantic import BaseModel, Field

class OrderSchema(BaseModel):
    bot_user_id: int = Field(ge=1, default=None)
    date_create: int = Field(default=None)
    status_id: int = Field(default=None)
    invoice_id: str = Field(max_length=20)

class OrderSchemaInDBSchema(OrderSchema):
    id: int = Field(ge=1)

conn = sqlite3.connect("db.db")
cur = conn.cursor()
cur.execute("""
SELECT * FROM orders;
""")
orders = []
for order in cur.fetchall():
    orders.append(
        Order(
            id=order[0],
            bot_user_id=order[1],
            date_create=order[2],
            status_id=order[3],
            invoice_id=order[4]
        )
    )
print(orders)