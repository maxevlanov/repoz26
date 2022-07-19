from pydantic import BaseModel, PostGresDSN


class DatabaseSchema(BaseModel):
    URL: PostgresDsn


class ConfigSchema(BaseModel):
    DATABASE: DatabaseSchema