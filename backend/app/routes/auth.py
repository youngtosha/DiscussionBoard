from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from app.services.auth_service import authenticate_user

router = APIRouter()

class LoginRequest(BaseModel):
    """Модель запроса на аутентификацию пользователя."""
    username: str
    password: str

@router.post("/login")
async def login(request: LoginRequest):
    """
    Аутентифицирует пользователя и возвращает токен доступа.

    **Параметры:**
    - `request` (LoginRequest): Данные для входа (логин и пароль).

    **Возвращает:**
    - `dict`: Токен доступа, если аутентификация успешна.

    **Ошибки:**
    - 401 Unauthorized: Неверное имя пользователя или пароль.
    """
    user = authenticate_user(request.username, request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверное имя пользователя или пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"access_token": user.token, "token_type": "bearer"}
