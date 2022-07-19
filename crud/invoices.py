from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models import Invoice, create_session
from schemas import InvoiceScheme, InvoiceInDBSchema


class CRUDInvoice:

    @staticmethod
    @create_session
    def add(invoice: InvoiceScheme, session: Session = None) -> InvoiceInDBSchema | None:
        invoice = Invoice(
            **invoice.dict()
        )
        session.add(invoice)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(invoice)
            return InvoiceInDBSchema(**invoice.__dict__)

    @staticmethod
    @create_session
    def get(invoice_id: int, session: Session = None) -> InvoiceInDBSchema | None:
        invoice = session.execute(
            select(Invoice).where(Invoice.id == invoice_id)
        )
        invoice = invoice.first()
        if invoice:
            return InvoiceInDBSchema(**invoice[0].__dict__)

    @staticmethod
    @create_session
    def get_all(status_id: int = None, session: Session = None) -> list[InvoiceInDBSchema] | None:
        if status_id:
            invoices = session.execute(
                select(Invoice).where(Invoice.status_id == status_id)
            )
        else:
            invoices = session.execute(
                select(Invoice)
            )
        return [InvoiceInDBSchema(**invoice[0].__dict__) for invoice in invoices]

    @staticmethod
    @create_session
    def update(invoice: InvoiceScheme, session: Session = None) -> None:
        session.execute(
            update(Invoice).where(Invoice.id == invoice.id).values(
                **invoice.dict()
            )
        )
        session.commit()

    @staticmethod
    @create_session
    def delete(invoice_id: int, session: Session = None) -> None:
        session.execute(
            delete(Invoice).where(Invoice.id == invoice.id)
        )
        session.commit()