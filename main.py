from fastapi import FastAPI
from routes import users
from services import create_db

app = FastAPI()
create_db()


app.include_router(users.router)
