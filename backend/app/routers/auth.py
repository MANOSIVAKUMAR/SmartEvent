from fastapi import APIRouter
from pydantic import BaseModel
from app.security import create_access_token

router = APIRouter()

class LoginRequest(BaseModel):
    user_id: int
    role: str

@router.post("/login")
def login(data: LoginRequest):
    # Demo login. Replace with your Phase 1 database authentication.
    token = create_access_token(data.user_id, data.role.upper())
    return {"access_token": token, "token_type": "bearer", "role": data.role.upper()}
