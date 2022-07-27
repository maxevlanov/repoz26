from datetime import datetime
from pydantic import BaseModel, Field

class OrderSchema(BaseModel):
    bot_user_id: int = Field(ge=1, min_length=1, default=None)
    date_create: datetime = Field(default=datetime.now())
    status_id: int = Field(ge=1, default=None)
    invoice_id: str = Field(min_length=1, max_length=20, ge=1, default=None)

class OrderInDBSchema(OrderSchema):
    id: int = Field(ge=1)