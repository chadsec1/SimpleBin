from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import paste
from app.database import init_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(paste.router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
