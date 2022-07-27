from pydantic import BaseModel, Field

class CategorySchema(BaseModel):
    parent_id: int = Field(ge=1, default=None)
    is_published: bool = Field(default=False)
    name_en: str
    name: str = Field(
        min_length=1,
        max_length=20,
        title="Name of category",
        description="name of category"
    )

class CategoryInDBSchema(CategorySchema):
    id: int = Field(ge=1)