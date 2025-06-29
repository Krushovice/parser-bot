from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class BotConfig(BaseModel):
    token: str
    admin_id: int


class WebConfig(BaseModel):
    base_url: str

    @property
    def get_webhook_url(self) -> str:
        """Возвращает URL вебхука с кодированием специальных символов."""
        return f"{self.base_url}/webhook"


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="APP__",
        env_nested_delimiter="__",
    )
    bot: BotConfig

    web: WebConfig


settings = Settings()
