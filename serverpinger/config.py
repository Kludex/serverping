from pydantic import BaseSettings


class Settings(BaseSettings):
    SERVER_NAME: str
    HOST: str
    PORT: int

    SLACK_API_TOKEN: str
    CHANNEL_ID: str

    PING_TIME: int

    class Config:
        case_sensitive = False
        env_file = ".env"


settings = Settings()
