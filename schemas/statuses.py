from pydantic import BaseModel, Field

class StatusSchema(BaseModel):
    name: str = Field(min_length=3, max_length=20)

class StatusSchemaInDBSchema(StatusSchema):
    id: int = Field(ge=1)