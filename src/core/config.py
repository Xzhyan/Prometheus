from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configurações base da ferramenta"""

    TOOL_NAME: str
    AUTHOR: str
    VERSION: str
    LANG: str
    DESC: str

    class Config:
        env_file = '.env'

settings = Settings()
