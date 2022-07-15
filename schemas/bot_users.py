import sqlite3
from pydantic import BaseModel, Field

class Bot_userSchema(BaseModel):
    is_blocked: bool = Field(default=False)
    balance: int = Field(default=None)
    language_id: int = Field(ge=1, default=None)

class Bot_userSchemaInDBSchema(Bot_userSchema):
    id: int = Field(ge=1)

conn = sqlite3.connect("db.db")
cur = conn.cursor()
cur.execute("""
SELECT * FROM bot_users;
""")
bot_users = []
for bot_user in cur.fetchall():
    bot_users.append(
        Bot_user(
            id=bot_user[0],
            is_blocked=bot_user[1],
            balance=bot_user[2],
            language_id=bot_user[3]
        )
    )
print(bot_users)