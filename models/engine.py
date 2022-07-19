from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import CONFIG


DATABASE_URI: str = CONFIG.DATABASE.URL
ENGINE = create_engine(DATABASE_URL)
Session = sessionmaker(bind=ENGINE)


def create_session(func):
    def wrapper(**kwargs):
        with Session() as session:
            return func(**kwargs, session=session)
    return wrapper