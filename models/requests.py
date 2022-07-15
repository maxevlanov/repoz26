class Category(BaseModel):
    id: int = Field(ge=1)
    parent_id: int = Field(ge=1, default=None)
    is_published: bool = Field(default=False)
    name_en: str
    name: str = Field(max_length=20)

conn = sqlite3.connect("db.db")
cur = conn.cursor()
cur.execute("""
SELECT * FROM categories;
""")
categories = []
for category in cur.fetchall():
    categories.append(
        Category(
            id=category[0],
            parent_id=category[1],
            is_published=category[2],
            name_en=category[3],
            name=category[4]
        )
    )
print(categories[1].name)