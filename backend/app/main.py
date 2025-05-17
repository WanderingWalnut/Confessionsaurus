from fastapi import FastAPI
from .models.confession import Base
from .db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"} 

@app.get("/")
async def root():
    return {"Message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"Message": f"Hello {name}"}



