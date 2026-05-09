from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TOOL_NAME: str
    VERSION: str
    AUTHOR: str

    class Config:
        env_file = '.env'


settings = Settings()
