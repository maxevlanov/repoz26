import sqlite3

conn = sqlite3.connect("db.db")
cur = conn.cursor()

class Language CRUD:

    @staticmethod
    def add(order:LanguageSchema) -> None:
        cur.execute("""
        INSERT INTO languages(language_code);
        """), (languages.language_code)
        conn.commit()

    @staticmethod
    def get(language_id:int) -> LanguageInDBSchema:
        pass

    @staticmethod
    def get_all() -> list[LanguageInDBSchema]:
        pass

    @staticmethod
    def update(language_id: int, language: LanguageSchema) -> None:
        pass

    @staticmethod
    def delete(language_id: int) -> None:
        pass
