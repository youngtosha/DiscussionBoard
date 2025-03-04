from fastapi import APIRouter, Depends
from app.services.auth_service import authenticate_user

router = APIRouter()

@router.post("/login")
async def login(username: str, password: str):
    return authenticate_user(username, password)
