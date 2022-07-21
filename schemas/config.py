from pydantic import BaseModel, PostGresDSN


class DatabaseSchema(BaseModel):
    URL: PostgresDsn
    ASYNC_URL: PostGresDSN


class ConfigSchema(BaseModel):
    DATABASE: DatabaseSchema