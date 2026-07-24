import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.predict import router as predict_router


app = FastAPI(
    title="CipherAnalytics API",
    description="AI-powered cryptographic algorithm identification platform",
    version="1.0.0"
)


# Allow requests from the Next.js frontend
# Add your deployed frontend URL via the FRONTEND_URL env var on Render
frontend_url = os.environ.get("FRONTEND_URL")

allowed_origins = [
    "http://localhost:3000",
]

if frontend_url:
    allowed_origins.append(frontend_url)


app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    predict_router,
    prefix="/api"
)


@app.get("/")
def home():
    return {
        "message": "CipherAnalytics API is running",
        "status": "active"
    }