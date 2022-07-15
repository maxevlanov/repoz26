import sqlite3
from pydantic import BaseModel, Field

class ProductSchema(BaseModel):
    category_id: int = Field(ge=1, default=None)
    price: int = Field(default=None)
    media: str
    total: int = Field(default=None)
    is_published: bool = Field(default=False)
    name_en: str
    name: str = Field(max_length=20)

class ProductSchemaInDBSchema(ProductSchema):
    id: int = Field(ge=1)

conn = sqlite3.connect("db.db")
cur = conn.cursor()
cur.execute("""
SELECT * FROM products;
""")
products = []
for product in cur.fetchall():
    products.append(
        Product(
            id=product[0],
            category_id=product[1],
            price=product[2],
            media=product[3],
            total=product[4],
            is_published=product[5],
            name_en=product[6],
            name=product[7]
        )
    )
print(products)