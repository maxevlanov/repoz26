import sqlite3

conn = sqlite3.connect("db.db")
cur = conn.cursor()

class Invoice CRUD:

    @staticmethod
    def add(invoice:InvoiceSchema) -> None:
        cur.execute("""
        INSERT INTO invoices(bot_user_id, date_created, total, status_id);
        """), (invoice.bot_user_id, invoice.date_created, invoice.total, invoice.status_id)
        conn.commit()

    @staticmethod
    def get(invoice_id:int) -> InvoiceInDBSchema:
        pass

    @staticmethod
    def get_all() -> list[InvoiceInDBSchema]:
        pass

    @staticmethod
    def update(invoice_id: int, invoice: InvoiceSchema) -> None:
        pass

    @staticmethod
    def delete(invoice_id: int) -> None:
        pass
