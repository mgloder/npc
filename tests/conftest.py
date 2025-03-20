import os

import pytest
from fastapi.testclient import TestClient

# Set the environment file path
os.environ["ENV_FILE"] = ".env.test"

# Import the app after setting the environment variable
from app.main import app  # noqa: E402


@pytest.fixture
def client() -> TestClient:
    """Create a test client for the FastAPI application."""
    return TestClient(app)


# Add other fixtures as needed
