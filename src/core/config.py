import os

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class BotConfig(BaseModel):
    token: str
    admin_id: int


class WebConfig(BaseModel):
    base_url: str


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env"),
        env_file_encoding="utf-8",
        env_prefix="__",
        env_nested_delimiter="__",

    )
    bot: BotConfig
    web: WebConfig

    @property
    def get_webhook_url(self) -> str:
        """Возвращает URL вебхука с кодированием специальных символов."""
        return f"{self.web.base_url}/webhook"


settings = Settings()