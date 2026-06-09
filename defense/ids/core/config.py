from pydantic_settings import BaseSettings, SettingsConfigDict
from core.constants import BASE_DIR


class Settings(BaseSettings):
    TOOL_NAME: str
    AUTHOR: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / '.env'
    )


settings = Settings()
