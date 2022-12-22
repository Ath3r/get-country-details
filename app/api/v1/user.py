from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.dep import get_db
from app.db import schema   
from app.service import user as user_service
from app.settings import settings

router = APIRouter()

# User Registration
@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(request: schema.User, db: Session = Depends(get_db)):
    user = user_service.get_user(db, request.username)
    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User with username {request.username} already exists")
    db_user = user_service.create_user(db=db, user=request)
    access_token = user_service.create_access_token(data={"sub": db_user.username}, secret=settings.SECRET, expiry=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return { 'access_token': access_token,'token_type': 'Bearer'}
    

# User Login
@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_service.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    access_token = user_service.create_access_token(data={"sub": user.username}, secret=settings.SECRET, expiry=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return { 'access_token': access_token,'token_type': 'Bearer'}


