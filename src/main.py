from fastapi import FastAPI
from database import Base, engine
from routers import example

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(example.router)
