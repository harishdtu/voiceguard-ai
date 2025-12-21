from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi_jwt_auth.exceptions import AuthJWTException

from app.auth import auth_router
from app.detector import detect_router

app = FastAPI(title="VoiceGuard AI")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for now (safe for demo)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(detect_router, prefix="/detect", tags=["Detection"])

# JWT exception handler
@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

@app.get("/")
def root():
    return {"status": "VoiceGuard API running"}
