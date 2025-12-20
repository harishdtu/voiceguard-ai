from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from dotenv import load_dotenv
from uuid import uuid4
from pathlib import Path
import os

load_dotenv()

auth_router = APIRouter()

# ================= JWT SETTINGS =================
class Settings(BaseModel):
    authjwt_secret_key: str

@AuthJWT.load_config
def get_config():
    secret = os.getenv("AUTHJWT_SECRET_KEY")
    if not secret:
        raise RuntimeError("AUTHJWT_SECRET_KEY is not set")
    return Settings(authjwt_secret_key=secret)

# ================= REQUEST MODELS =================
class LoginRequest(BaseModel):
    username: str
    password: str

# ================= AUTH ROUTES =================
@auth_router.post("/login")
def login(user: LoginRequest, Authorize: AuthJWT = Depends()):
    access_token = Authorize.create_access_token(subject=user.username)
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@auth_router.get("/protected")
def protected(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    user = Authorize.get_jwt_subject()
    return {
        "message": "JWT is valid",
        "user": user
    }

# ================= DIRECTORIES =================
AUDIO_DIR = Path("uploads/audio")
VIDEO_DIR = Path("uploads/video")

AUDIO_DIR.mkdir(parents=True, exist_ok=True)
VIDEO_DIR.mkdir(parents=True, exist_ok=True)

# ================= AUDIO UPLOAD =================
@auth_router.post("/upload-audio")
def upload_audio(
    file: UploadFile = File(...),
    Authorize: AuthJWT = Depends()
):
    Authorize.jwt_required()
    user = Authorize.get_jwt_subject()

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file received. Use form-data with key='file'"
        )

    if not file.filename.lower().endswith((".wav", ".mp3", ".m4a")):
        raise HTTPException(
            status_code=400,
            detail="Only audio files (.wav, .mp3, .m4a) are allowed"
        )

    file_id = f"{uuid4()}_{file.filename}"
    file_path = AUDIO_DIR / file_id

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return {
        "message": "Audio uploaded successfully",
        "filename": file_id,
        "uploaded_by": user
    }

# ================= VIDEO UPLOAD =================
@auth_router.post("/upload-video")
def upload_video(
    file: UploadFile = File(...),
    Authorize: AuthJWT = Depends()
):
    Authorize.jwt_required()
    user = Authorize.get_jwt_subject()

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file received. Use form-data with key='file'"
        )

    if not file.filename.lower().endswith((".mp4", ".mov", ".avi", ".mkv")):
        raise HTTPException(
            status_code=400,
            detail="Only video files (.mp4, .mov, .avi, .mkv) are allowed"
        )

    file_id = f"{uuid4()}_{file.filename}"
    file_path = VIDEO_DIR / file_id

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return {
        "message": "Video uploaded successfully",
        "filename": file_id,
        "uploaded_by": user
    }

import random
from datetime import datetime

def mock_inference(media_type: str):
    """
    Mock ML inference function.
    Replace with real ML model later.
    """
    return {
        "media_type": media_type,
        "result": random.choice(["real", "fake"]),
        "confidence": round(random.uniform(0.65, 0.99), 2),
        "model": "VoiceGuardAI-Mock-v1",
        "processed_at": datetime.utcnow().isoformat() + "Z"
    }

@auth_router.post("/analyze-audio")
def analyze_audio(
    file: UploadFile = File(...),
    Authorize: AuthJWT = Depends()
):
    Authorize.jwt_required()
    user = Authorize.get_jwt_subject()

    if not file.filename:
        raise HTTPException(status_code=400, detail="No audio file provided")

    if not file.filename.lower().endswith((".wav", ".mp3", ".m4a")):
        raise HTTPException(
            status_code=400,
            detail="Only audio files (.wav, .mp3, .m4a) are allowed"
        )

    inference = mock_inference(media_type="audio")

    return {
        "status": "success",
        "user": user,
        "filename": file.filename,
        "analysis": {
            "result": inference["result"],
            "confidence": inference["confidence"]
        },
        "model": inference["model"],
        "processed_at": inference["processed_at"]
    }

@auth_router.post("/analyze-video")
def analyze_video(
    file: UploadFile = File(...),
    Authorize: AuthJWT = Depends()
):
    Authorize.jwt_required()
    user = Authorize.get_jwt_subject()

    if not file.filename:
        raise HTTPException(status_code=400, detail="No video file provided")

    if not file.filename.lower().endswith((".mp4", ".mov", ".avi", ".mkv")):
        raise HTTPException(
            status_code=400,
            detail="Only video files (.mp4, .mov, .avi, .mkv) are allowed"
        )

    inference = mock_inference(media_type="video")

    return {
        "status": "success",
        "user": user,
        "filename": file.filename,
        "analysis": {
            "result": inference["result"],
            "confidence": inference["confidence"]
        },
        "model": inference["model"],
        "processed_at": inference["processed_at"]
    }
