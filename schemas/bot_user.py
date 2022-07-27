from pydantic import BaseModel, Field

class BotUserSchema(BaseModel):
    is_blocked: bool = Field(default=False)
    balance: int = Field(default=None)
    language_id: int = Field(ge=1, default=None)

class BotUserInDBSchema(BotUserSchema):
    id: int = Field(ge=1, min_length=1)