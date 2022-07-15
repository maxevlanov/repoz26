import sqlite3
from pydantic import BaseModel, Field

class StatusSchema(BaseModel):
    name: str = Field(max_length=20)

class StatusSchemaInDBSchema(StatusSchema):
    id: int = Field(ge=1)

conn = sqlite3.connect("db.db")
cur = conn.cursor()
cur.execute("""
SELECT * FROM statuses;
""")
statuses = []
for status in cur.fetchall():
    statuses.append(
        Status(
            id=status[0],
            name=status[1]
        )
    )
print(statuses)