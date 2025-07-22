from fastapi import FastAPI
from app.api import task
from app.db.base import Base
from app.db.database import engine
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(task.router)
@app.get("/")
async def root():
    return {"message": "Hello World"}
