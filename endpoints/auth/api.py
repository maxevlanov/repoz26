from datetime import datetime, timedelta

from fastapi import APIRouter, HTTPException
from jose import JWTError, jwt
from passlib.context import CryptContext

from crud_async import CRUDUser
from schemas import UserRegisterSchema, UserSchema, pwd_context
from core.config import CONFIG

pwd_context = CryptContext(schemas=["bcrypt"], deprecated="auto")
auth_router = APIRouter(prefix="/auth")


async def create_access_token(username: str) -> str:
    data = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(minutes=CONFIG.AUTH.ACCESS_TOKEN_EXPIRE_MINUTES)}
    encoded_jwt = jwt.encode(data, CONFIG.AUTH.SECRET_KEY, algorithm=CONFIG.AUTH.ALGORITHM)
    return encoded_jwt


@auth_router.post("/register")
async def register_user(user: UserRegisterSchema):
    hashed_password = pwd_context.hash(user.password)
    user = UserSchema(username=user.username, hashed_password=user.password)
    if await CRUDUser.add(user=user):
        user_access_token = await create_access_token(username=user.username)
        return {"token": user_access_token}
    else:
        raise HTTPException(status_code=400, detail="user is exists or invalid username or password")


@auth_router.post("/login")
async def login(user: UserRegisterSchema):
    user_in_db = await CRUDUser.get_by_username(username=user.username)
    if user_in_db:
        if pwd_context.verify(user.password, user_in_db.hashed_password):
            return {"token": await create_access_token(username=user.username)}
        else:
            raise HTTPException(status_code=401, detail="invalid password")
    else:
        raise HTTPException(status_code=404, detail="user not found")