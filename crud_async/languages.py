from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models import Language, create_async_session
from schemas import LanguageScheme, LanguageInDBSchema


class CRUDLanguage:

    @staticmethod
    @create_async_session
    async def add(language: LanguageScheme, session: AsyncSession = None) -> LanguageInDBSchema | None:
        language = Language(
            **language.dict()
        )
        session.add(language)
        try:
            await session.commit()
        except IntegrityError:
            return None
        else:
            await session.refresh(language)
            return LanguageInDBSchema(**language.__dict__)

    @staticmethod
    @create_async_session
    async def get(language_id: int, session: AsyncSession = None) -> LanguageInDBSchema | None:
        language = await session.execute(
            select(Language).where(Language.id == language_id)
        )
        language = language.first()
        if language:
            return LanguageInDBSchema(**language[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(language_id: int = None, session: AsyncSession = None) -> list[LanguageInDBSchema] | None:
        if language_id:
            languages = await session.execute(
                select(Language).where(Language.language_id == language_id)
                .where(Language.language_id == language_id)
            )
        else:
            languages = await session.execute(
                select(Language)
            )
        return [LanguageInDBSchema(**language[0].__dict__) for language in languages]

    @staticmethod
    @create_async_session
    async def update(language: LanguageInDBSchema, session: AsyncSession = None) -> None:
        await session.execute(
            update(Language).where(Language.id == language.id).values(
                **language.dict()
            )
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def delete(language_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(Language).where(Language.id == language.id)
        )
        await session.commit()