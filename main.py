from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import get_pool, close_pool
from routers import fasilitas

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Starting server... 🚀")
    
    # connect database
    await get_pool()
    print("✅ Database connected ✅")

    yield

    # disconnect database
    await close_pool()
    print("❌ Database disconnected ❌")

app = FastAPI(
    title="WebGIS API",
    description="API untuk data spasial",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(fasilitas.router)

@app.get("/")
def root():
    return {"message": "API jalan 🚀"}