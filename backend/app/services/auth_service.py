from app.models.user import User
from app.database import SessionLocal

def authenticate_user(username: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    if user and user.password_hash == password:  # TODO: Replace with hashing
        return {"message": "Login successful"}
    return {"error": "Invalid credentials"}
