from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = {"env_file": ".env"}
    bot_token: str
    bot_name: str
    db_url: str
    {% if cookiecutter.payment_service == "Yookassa" %}
    yookassa_shop_id: str
    yookassa_secret_key: str
    {% endif %}