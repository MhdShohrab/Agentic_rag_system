# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routes (we will connect them)
from routes.ask import router as ask_router
from routes.upload import router as upload_router

# Create FastAPI app
app = FastAPI(                       #this app is written in, uvicorn main:app --reload
    title="Agentic AI Backend",
    description="Multi-tool AI Agent with RAG + Memory",
    version="1.0.0"
)

# Enable CORS (IMPORTANT for frontend later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(ask_router)
app.include_router(upload_router)

# Basic test route
@app.get("/")
def home():
    return {"message": "AI Agent Backend Running"}