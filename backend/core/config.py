from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Article Management"
    API_VERSION: str = "v1"
    MONGO_URL: str = os.getenv("mongo_url")
    DB_NAME: str = "articles_db"

    class Config:
        env_file = ".env"


settings = Settings()
