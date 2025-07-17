from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    app_name: str = "Access API"
    app_version: str = "1.0.0"
    app_description: str = "FastAPI application for access management"
    debug: bool = True
    
    host: str = "0.0.0.0"
    port: int = 8000
    
    # For simplicity, using SQLite. Change to PostgreSQL for production
    database_url: str = "sqlite:///./access_api.db"
    
    secret_key: str = "your-secret-key-here-change-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    allowed_origins: List[str] = ["http://localhost:3000", "http://localhost:8080", "http://localhost:8000"]

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()