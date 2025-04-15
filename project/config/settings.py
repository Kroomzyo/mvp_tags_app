from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    PHOTO_HELLO_ID: str = "photo_id"
    BASE_URL_INFO: str = "url"
    BASE_URL_DOCS: str = "url"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
