from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="My first API",
    description="Mi primera API, Khe mosion",
    version="0.0.1",
    openapi_tags=[
        {
            "name": "users",
            "description": "Routes Users associating"
        }
    ]
)

app.include_router(user)