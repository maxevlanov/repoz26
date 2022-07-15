import sqlite3

conn = sqlite3.connect("db.db")
cur = conn.cursor()

class Status CRUD:

    @staticmethod
    def add(status:CategorySchema) -> None:
        cur.execute("""
        INSERT INTO statuses(name);
        """), (status.name)
        conn.commit()

    @staticmethod
    def get(status_id:int) -> StatusInDBSchema:
        pass

    @staticmethod
    def get_all() -> list[StatusInDBSchema]:
        pass

    @staticmethod
    def update(status_id: int, status: StatusSchema) -> None:
        pass

    @staticmethod
    def delete(status_id: int) -> None:
        pass