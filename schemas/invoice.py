from datetime import datetime
from pydantic import BaseModel, Field

class InvoiceSchema(BaseModel):
    bot_user_id: int = Field(ge=1, default=None)
    date_create: datetime = Field(default=datetime.now())
    total: int = Field(default=None)
    status_id: int = Field(default=None, ge=1)

class InvoiceInDBSchema(InvoiceSchema):
    id: int = Field(ge=1)