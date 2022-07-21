from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models import Invoice, create_async_session
from schemas import InvoiceScheme, InvoiceInDBSchema


class CRUDInvoice:

    @staticmethod
    @create_async_session
    async def add(invoice: InvoiceScheme, session: AsyncSession = None) -> InvoiceInDBSchema | None:
        invoice = Invoice(
            **invoice.dict()
        )
        session.add(invoice)
        try:
            await session.commit()
        except IntegrityError:
            return None
        else:
            await session.refresh(invoice)
            return InvoiceInDBSchema(**invoice.__dict__)

    @staticmethod
    @create_async_session
    async def get(invoice_id: int, session: AsyncSession = None) -> InvoiceInDBSchema | None:
        invoice = await session.execute(
            select(Invoice).where(Invoice.id == invoice_id)
        )
        invoice = invoice.first()
        if invoice:
            return InvoiceInDBSchema(**invoice[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(status_id: int = None, session: AsyncSession = None) -> list[InvoiceInDBSchema] | None:
        if status_id:
            invoices = await session.execute(
                select(Invoice).where(Invoice.status_id == status_id)
                .where(Invoice.status_id == status_id)
            )
        else:
            invoices = await session.execute(
                select(Invoice)
            )
        return [InvoiceInDBSchema(**invoice[0].__dict__) for invoice in invoices]

    @staticmethod
    @create_async_session
    async def update(invoice: InvoiceScheme, session: AsyncSession = None) -> None:
        await session.execute(
            update(Invoice).where(Invoice.id == invoice.id).values(
                **invoice.dict()
            )
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def delete(invoice_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(Invoice).where(Invoice.id == invoice.id)
        )
        await session.commit()