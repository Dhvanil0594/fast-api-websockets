from pydantic_settings import BaseSettings, SettingsConfigDict
from logger import logger
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    DEBUG: bool = False
    PROFILING_ENABLED: bool = False
    OPENAPI_DOCS_URL: str | None = None
    OPENAPI_REDOC_URL: str | None = None
    MASTER_DB_USER: str
    MASTER_DB_PASSWORD: str
    MASTER_DB_HOSTNAME: str
    MASTER_DB_PORT: str
    MASTER_DB_NAME: str
    JWT_SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 500
    ALGORITHM: str


settings = Settings()