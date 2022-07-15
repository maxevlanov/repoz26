import sqlite3

conn = sqlite3.connect("db.db")
cur = conn.cursor()

class Bot_user CRUD:

    @staticmethod
    def add(bot_user:Bot_userSchema) -> None:
        cur.execute("""
        INSERT INTO categories(is_blocked,  balance, language_id);
        """), (bot_user.is_blicked, bot_user.balance, bot_user.language_id)
        conn.commit()

    @staticmethod
    def get(bot_user_id:int) -> Bot_userInDBSchema:
        pass

    @staticmethod
    def get_all() -> list[Bot_userInDBSchema]:
        pass

    @staticmethod
    def update(bot_user_id: int, bot_user: Bot_userSchema) -> None:
        pass

    @staticmethod
    def delete(bot_user_id: int) -> None:
        pass