from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models import BotUser, create_async_session
from schemas import BotUserSchema, BotUserInDBSchema


class CRUDBotUser:

    @staticmethod
    @create_async_session
    async def add(bot_user: BotUserSchema, session: AsyncSession = None) -> BotUserInDBSchema | None:
        bot_user = BotUser(
            **bot_user.dict()
        )
        session.add(bot_user)
        try:
            await session.commit()
        except IntegrityError:
            return None
        else:
            await session.refresh(bot_user)
            return BotUserInDBSchema(**bot_user.__dict__)

    @staticmethod
    @create_async_session
    async def get(bot_user_id: int, session: AsyncSession = None) -> BotUserInDBSchema | None:
        bot_user = await session.execute(
            select(BotUser).where(BotUser.id == bot_user_id)
        )
        bot_user = bot_user.first()
        if bot_user:
            return BotUserInDBSchema(**bot_user[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(language_id: int = None, session: AsyncSession = None) -> list[BotUserInDBSchema] | None:
        if language_id:
            bot_users = await session.execute(
                select(BotUser).where(BotUser.language_id == language_id)
                .where(BotUser.language_id == language_id)
            )
        else:
            bot_users = await session.execute(
                select(BotUser)
            )
        return [BotUserInDBSchema(**bot_user[0].__dict__) for bot_user in bot_users]

    @staticmethod
    @create_async_session
    async def update(bot_user: BotUserSchema, session: AsyncSession = None) -> None:
        await session.execute(
            update(BotUser).where(BotUser.id == bot_user.id).values(
                **bot_user.dict()
            )
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def delete(bot_user_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(BotUser).where(BotUser.id == bot_user_id)
        )
        await session.commit()