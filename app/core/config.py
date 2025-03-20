from typing import List
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "NPC Game API"
    
    # CORS
    CORS_ORIGINS: List[AnyHttpUrl] = []
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings() 