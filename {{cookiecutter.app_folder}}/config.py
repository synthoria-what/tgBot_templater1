from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = {"env_file": ".env"}
    bot_token: str
    bot_name: str
    db_url: str