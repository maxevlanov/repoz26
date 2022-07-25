from pydantic import BaseModel, Field

class ProductSchema(BaseModel):
    category_id: int = Field(ge=1, default=None)
    price: float
    media: str
    total: int = Field(ge=0, default=None)
    is_published: bool = Field(default=False)
    name_en: str
    name: str = Field(
        min_length=3,
        max_length=20,
        title="Name of product",
        description="name of product"
    )

class ProductSchemaInDBSchema(ProductSchema):
    id: int = Field(ge=1)