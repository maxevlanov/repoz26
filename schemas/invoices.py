import sqlite3
from pydantic import BaseModel, Field

class InvoiceSchema(BaseModel):
    bot_user_id: int = Field(ge=1, default=None, min_length=1)
    date_create: int = Field(default=None)
    total: int = Field(default=None)
    status_id: int = Field(default=None)

class InvoiceSchemaInDBSchema(InvoiceSchema):
    id: int = Field(ge=1, min_length=1)

conn = sqlite3.connect("db.db")
cur = conn.cursor()
cur.execute("""
SELECT * FROM invoices;
""")
invoices = []
for invoice in cur.fetchall():
    invoices.append(
        Invoice(
            id=invoice[0],
            bot_user_id=invoice[1],
            date_create=invoice[2],
            total=invoice[3],
            status_id=invoice[4]
        )
    )
print(invoices)