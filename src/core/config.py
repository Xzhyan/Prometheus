from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configurações base da ferramenta"""

    TOOL_NAME: str
    AUTHOR: str
    VERSION: str
    LANG: str
    DESC: str

    model_config = SettingsConfigDict(
        env_file='.env'
    )


settings = Settings()
