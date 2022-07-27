from pydantic import BaseModel, Field

class LanguageSchema(BaseModel):
    language_code: int = Field(ge=1, default=None, min_length=3, max_length=12)

class LanguageInDBSchema(LanguageSchema):
    id: int = Field(ge=1)