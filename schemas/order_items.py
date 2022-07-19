from pydantic import BaseModel, Field

class Order_ItemSchema(BaseModel):
    order_id: int = Field(ge=1, default=None)
    product_id: int = Field(ge=1, default=None)
    total: int = Field(ge=0, default=None)

class Order_ItemSchemaInDBSchema(Order_ItemSchema):
    id: int = Field(ge=1)