from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.endpoints import npc
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="API for generic NPC behavior in games",
    version="0.1.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(npc.router, prefix=settings.API_V1_STR)


@app.get("/")
async def root():
    return {"message": "Welcome to the NPC Game API. See /docs for API documentation."} 