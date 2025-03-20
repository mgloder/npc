import json
from typing import Any, List

from pydantic import Field, validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "NPC Game API"

    # CORS
    CORS_ORIGINS: Any = Field(
        default=["http://localhost:3000", "http://localhost:8000"],
        description="List of CORS origins",
    )

    @validator("CORS_ORIGINS", pre=True)
    def parse_cors_origins(cls, v: Any) -> List[str]:
        if isinstance(v, str):
            # Try to parse as JSON first
            try:
                parsed = json.loads(v)
                if isinstance(parsed, list):
                    return parsed
            except json.JSONDecodeError:
                # Fall back to comma-separated format
                if "," in v:
                    return [origin.strip() for origin in v.split(",")]
                # If it's a single URL, return it as a list
                return [v.strip()]
        elif isinstance(v, list):
            return v
        # Default to empty list if none of the above work
        return []

    @validator("CORS_ORIGINS")
    def validate_cors_origins(cls, v: Any) -> List[str]:
        if not isinstance(v, list):
            return []
        return [str(origin) for origin in v]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
