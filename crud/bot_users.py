from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models import Bot_user, create_session
from schemas import Bot_userSchema, Bot_userInDBSchema


class CRUDBot_user:

    @staticmethod
    @create_session
    def add(bot_user: Bot_userSchema, session: Session = None) -> Bot_userInDBSchema | None:
        bot_user = Bot_user(
            **bot_user.dict()
        )
        session.add(bot_user)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(bot_user)
            return Bot_userInDBSchema(**bot_user.__dict__)

    @staticmethod
    @create_session
    def get(bot_user_id: int, session: Session = None) -> Bot_userInDBSchema | None:
        bot_user = session.execute(
            select(Bot_user).where(Bot_user.id == bot_user_id)
        )
        bot_user = bot_user.first()
        if bot_user:
            return Bot_userInDBSchema(**bot_user[0].__dict__)

    @staticmethod
    @create_session
    def get_all(language_id: int = None, session: Session = None) -> list[Bot_userInDBSchema] | None:
        if language_id:
            bot_users = session.execute(
                select(Bot_user).where(Bot_user.language_id == language_id)
            )
        else:
            bot_users = session.execute(
                select(Bot_user)
            )
        return [Bot_userInDBSchema(**bot_user[0].__dict__) for bot_user in bot_users]

    @staticmethod
    @create_session
    def update(bot_user: Bot_userSchema, session: Session = None) -> None:
        session.execute(
            update(Bot_user).where(Bot_user.id == bot_user.id).values(
                **bot_user.dict()
            )
        )
        session.commit()

    @staticmethod
    @create_session
    def delete(bot_user_id: int, session: Session = None) -> None:
        session.execute(
            delete(Bot_user).where(Bot_user.id == bot_user_id)
        )
        session.commit()