import os
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = Field(..., env="DB_URL")
    PROJECT_NAME: str = "PRJ_NAME"
    # x minutes * x hours * x days = x days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(..., env="ACCESS_TOKEN_EXPIRE_MINUTES")
    TOKEN_URL: str = "/api/v1/user/login"
    SECRET : str = Field(..., env="SECRET")
    ALGORITHM : str = Field(..., env="ALGORITHM")
    class Config:
        case_sensitive = True

settings = Settings()