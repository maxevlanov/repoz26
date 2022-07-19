from pydantic import BaseModel, Field

class OrderItemSchema(BaseModel):
    order_id: int = Field(ge=1, default=None)
    product_id: int = Field(ge=1, default=None)
    total: int = Field(ge=0, default=None)

class OrderItemSchemaInDBSchema(OrderItemSchema):
    id: int = Field(ge=1)