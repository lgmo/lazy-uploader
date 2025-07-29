from pydantic import Field, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    storage_base_url: HttpUrl = Field(alias="STORAGE_BASE_URL")
    db_url: str = Field(alias="DB_URL")
    db_port: int = Field(alias="DB_PORT")
    environment: str = Field(alias="ENVIRONMENT", default="development")

    model_config = SettingsConfigDict(env_file=".env")


_settings: Settings | None = None


def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
