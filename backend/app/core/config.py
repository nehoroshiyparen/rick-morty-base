from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME : str = 'rick&morty-base'
    DEBUG: bool = True

    APP_PORT: int
    APP_HOST: str

    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()