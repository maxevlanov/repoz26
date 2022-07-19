from datetime import datetime
from pydantic import BaseModel, Field

class InvoiceSchema(BaseModel):
    bot_user_id: int = Field(ge=1, default=None, min_length=1)
    date_create: datetime = Field(default=datetime.now())
    total: int = Field(default=None)
    status_id: int = Field(default=None)

class InvoiceSchemaInDBSchema(InvoiceSchema):
    id: int = Field(ge=1, min_length=1)