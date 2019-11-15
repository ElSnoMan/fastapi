from fastapi import FastAPI
from .routers import users

app = FastAPI()

app.include_router(
    router=users.router,
    prefix='/users'
)

# $ uvicorn app.main:app --reload
# Then go to -> localhost:8000/docs


