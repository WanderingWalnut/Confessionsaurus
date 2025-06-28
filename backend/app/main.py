from fastapi import FastAPI

# It's like saying "get the router from the api folder and call it api_router"
from .api import router as api_router

from .db.session import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include the main API router with prefix, It's like saying "use this router, and put all its routes under /api"
app.include_router(api_router, prefix="/api")

@app.get("/health")
def health_check():
    return {"status": "ok"} 

@app.get("/")
async def root():
    return {"Message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"Message": f"Hello {name}"}



