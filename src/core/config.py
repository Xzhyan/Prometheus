from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyUrl
from pathlib import Path


class Settings(BaseSettings):
    """Configurações base da ferramenta"""

    # Configuração da ferramenta
    TOOL_NAME: str
    AUTHOR: str
    VERSION: str
    LANG: str
    DESC: str


    # EasySharing
    EASY_PATH: Path
    EASY_SERVER_IP: str

    BIT_LINK_CHECKER_URL: AnyUrl
    VIRUS_TOTAL_URL: AnyUrl


    model_config = SettingsConfigDict(
        env_file='.env'
    )


settings = Settings()
