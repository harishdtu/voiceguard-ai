import random
from fastapi import APIRouter, UploadFile, File, Depends
from fastapi_jwt_auth import AuthJWT

detect_router = APIRouter()

@detect_router.post("/media")
def detect_media(
    file: UploadFile = File(...),
    Authorize: AuthJWT = Depends()
):
    Authorize.jwt_required()

    confidence = round(random.uniform(0.6, 0.99), 2)
    prediction = "FAKE" if confidence > 0.75 else "REAL"

    return {
        "filename": file.filename,
        "prediction": prediction,
        "confidence": confidence,
        "model": "VoiceGuardAI-Mock-v1"
    }

