from jose import jwt
from fastapi import HTTPException, status
from app.db import schema
from app.settings import settings
from jose import JWTError
from app.service.user import get_user
from sqlalchemy.orm import Session

def verify_token(db: Session,token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schema.TokenData(username=username)
    except JWTError as e:
        print("jwt error", e)
        raise credentials_exception
    user = get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
