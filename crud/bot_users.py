from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models import BotUser, create_session
from schemas import BotUserSchema, BotUserInDBSchema


class CRUDBotUser:

    @staticmethod
    @create_session
    def add(bot_user: BotUserSchema, session: Session = None) -> BotUserInDBSchema | None:
        bot_user = BotUser(
            **bot_user.dict()
        )
        session.add(bot_user)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(bot_user)
            return BotUserInDBSchema(**bot_user.__dict__)

    @staticmethod
    @create_session
    def get(bot_user_id: int, session: Session = None) -> BotUserInDBSchema | None:
        bot_user = session.execute(
            select(BotUser).where(BotUser.id == bot_user_id)
        )
        bot_user = bot_user.first()
        if bot_user:
            return BotUserInDBSchema(**bot_user[0].__dict__)

    @staticmethod
    @create_session
    def get_all(language_id: int = None, session: Session = None) -> list[BotUserInDBSchema] | None:
        if language_id:
            bot_users = session.execute(
                select(BotUser).where(BotUser.language_id == language_id)
            )
        else:
            bot_users = session.execute(
                select(BotUser)
            )
        return [BotUserInDBSchema(**bot_user[0].__dict__) for bot_user in bot_users]

    @staticmethod
    @create_session
    def update(bot_user: BotUserSchema, session: Session = None) -> None:
        session.execute(
            update(BotUser).where(BotUser.id == bot_user.id).values(
                **bot_user.dict()
            )
        )
        session.commit()

    @staticmethod
    @create_session
    def delete(bot_user_id: int, session: Session = None) -> None:
        session.execute(
            delete(BotUser).where(BotUser.id == bot_user_id)
        )
        session.commit()