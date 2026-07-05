"""
This file starts the MinePilot Electrical backend.

It creates a FastAPI app, allows the local frontend to connect to it,
and provides simple test routes to check that the backend is running.
"""


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create the FastAPI backend application
app = FastAPI(
    title="MinePilot Electrical API",
    description="Backend API for MinePilot Electrical engineering automation platform.",
    version="0.1.0",
)

# Allow the Next.js frontend to call this backend during local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Basic route to confirm the API is running
@app.get("/")
def root():
    return {
        "message": "MinePilot Electrical API is running",
        "status": "ok",
    }


# Health check route for frontend/backend connection testing
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }