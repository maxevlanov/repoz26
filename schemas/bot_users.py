from pydantic import BaseModel, Field

class Bot_userSchema(BaseModel):
    is_blocked: bool = Field(default=False)
    balance: int = Field(default=None)
    language_id: int = Field(ge=1, default=None)

class Bot_userSchemaInDBSchema(Bot_userSchema):
    id: int = Field(ge=1, min_length=1)