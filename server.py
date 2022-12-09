import uvicorn

from fastapi import FastAPI

from src.app import create_app
from src.models import postgres


app = create_app()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)
