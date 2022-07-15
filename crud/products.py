import sqlite3

conn = sqlite3.connect("db.db")
cur = conn.cursor()

class Product CRUD:

    @staticmethod
    def add(product:ProductSchema) -> None:
        cur.execute("""
        INSERT INTO products(category_id, price, media, total, is_published, name_en, name);
        """), (product.category_id, product.price, product.media, product.total, product.is_published,
               product.name_en, product.name)
        conn.commit()

    @staticmethod
    def get(product_id:int) -> ProductInDBSchema:
        pass

    @staticmethod
    def get_all() -> list[ProductInDBSchema]:
        pass

    @staticmethod
    def update(product_id: int, product: ProductSchema) -> None:
        pass

    @staticmethod
    def delete(product_id: int) -> None:
        pass