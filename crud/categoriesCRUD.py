import sqlite3

conn = sqlite3.connect("db.db")
cur = conn.cursor()

class CategoryCRUD:

    @staticmethod
    def add(category:CategorySchema) -> None:
        cur.execute("""
        INSERT INTO categories(parent_id, is_published, name_en, name);
        """), (category.parent_id, category.is_published, category.name_en, category.name)
        conn.commit()

    @staticmethod
    def get(category_id:int) -> CategoryInDBSchema:
        pass

    @staticmethod
    def get_all() -> list[CategoryInDBSchema]:
        pass

    @staticmethod
    def update(category_id: int, category: CategorySchema) -> None:
        pass

    @staticmethod
    def delete(category_id: int) -> None:
        pass