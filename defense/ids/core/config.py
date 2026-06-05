from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TOOL_NAME: str
    AUTHOR: str

    class Config:
        env_file = '.env'
