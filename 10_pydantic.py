from pydantic import BaseModel, Field, datetime

from typing import Optional

class MagazineSceme(BaseModel):
    categories: str = Field(
        alias="categories",
        max_length=24,
        min_length=8
    )
    products: str = Field(
        alias="products",
        max_length=24,
        min_length=8
    )
    order_items: str = Field(
        alias="order_items",
        max_length=24,
        min_length=8
    )
    orders: str = Field(
        alias="orders",
        max_length=24,
        min_length=8
    )
    statyses: str = Field(
        alias="statuses",
        max_length=24,
        min_length=8
    )
    bot_users: str = Field(
        alias="bot_users",
        max_length=24,
        min_length=8
    )
    languages: str = Field(
        alias="languages",
        max_length=24,
        min_length=8
    )
    invoices: int = Field(
        alias="invoices",
        max_length=24,
        min_length=8
    )

@validator("languages")