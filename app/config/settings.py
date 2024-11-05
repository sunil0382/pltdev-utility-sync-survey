from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    POSTGRESQL_CONNECTION_STRING: str
    ADDC_SCHEMA: str
    AADC_SCHEMA: str
    ENV: str

    class Config:
        env_file = ".env"


settings = Settings()  # type: ignore[call-arg]


def get_current_schema() -> str:
    if settings.ENV == "ADDC":
        return settings.ADDC_SCHEMA
    elif settings.ENV == "AADC":
        return settings.AADC_SCHEMA
    else:
        return settings.ADDC_SCHEMA


SCHEMA = get_current_schema()
