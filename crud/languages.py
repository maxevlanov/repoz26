from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from models import Language, create_session
from schemas import LanguageScheme, LanguageInDBSchema


class CRUDLanguage:

    @staticmethod
    @create_session
    def add(language: LanguageScheme, session: Session = None) -> LanguageInDBSchema | None:
        language = Language(
            **language.dict()
        )
        session.add(language)
        try:
            session.commit()
        except IntegrityError:
            return None
        else:
            session.refresh(language)
            return LanguageInDBSchema(**language.__dict__)

    @staticmethod
    @create_session
    def get(language_id: int, session: Session = None) -> LanguageInDBSchema | None:
        language = session.execute(
            select(Language).where(Language.id == language_id)
        )
        language = language.first()
        if language:
            return LanguageInDBSchema(**language[0].__dict__)

    @staticmethod
    @create_session
    def get_all(language_id: int = None, session: Session = None) -> list[LanguageInDBSchema] | None:
        if language_id:
            languages = session.execute(
                select(Language).where(Language.language_id == language_id)
            )
        else:
            languages = session.execute(
                select(Language)
            )
        return [LanguageInDBSchema(**language[0].__dict__) for language in languages]

    @staticmethod
    @create_session
    def update(language: LanguageInDBSchema, session: Session = None) -> None:
        session.execute(
            update(Language).where(Language.id == language.id).values(
                **language.dict()
            )
        )
        session.commit()

    @staticmethod
    @create_session
    def delete(language_id: int, session: Session = None) -> None:
        session.execute(
            delete(Language).where(Language.id == language.id)
        )
        session.commit()