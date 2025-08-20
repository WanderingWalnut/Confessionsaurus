from fastapi import FastAPI
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware

# It's like saying "get the router from the api folder and call it api_router"
from .api import router as api_router

from .db.session import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI()
handler = Mangum(app)

origins = [
    "http://localhost:5173", # Local development
    "https://confessionsaurus.com" # Production frontend
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, # Only needed for auth/cookies
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

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



