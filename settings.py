# settings.py
from pydantic_settings import BaseSettings
from pydantic import ValidationError, field_validator


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str

    @field_validator("ENVIRONMENT", mode="before")
    def validate_environment(cls, value):
        allowed_values = {"dev", "test", "prod"}
        if value not in allowed_values:
            raise ValidationError(
                f"Invalid environment: {value}. Must be one of {allowed_values}."
            )
        return value
