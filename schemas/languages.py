import sqlite3
from pydantic import BaseModel, Field

class LanguageSchema(BaseModel):
    language_code: int = Field(ge=1, default=None, min_length=3, max_length=12)

class LanguageSchemaInDBSchema(LanguageSchema):
    id: int = Field(ge=1)

conn = sqlite3.connect("db.db")
cur = conn.cursor()
cur.execute("""
SELECT * FROM languages;
""")
languages = []
for language in cur.fetchall():
    languages.append(
        Language(
            id=language[0],
            language_code=language[1]
        )
    )
print(languages)