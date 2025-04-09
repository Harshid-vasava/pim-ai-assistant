from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="PIM AI Assistant")

app.include_router(router)
