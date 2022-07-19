from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL: str = "postgresql://belhard:belhard@localhost:5432/belhard"
ENGINE = create_engine(DATABASE_URL)
Session = sessionmaker(bind=ENGINE)


def create_session(func):
    def wrapper(**kwargs):
        with Session() as session:
            return func(**kwargs, session=session)
    return wrapper