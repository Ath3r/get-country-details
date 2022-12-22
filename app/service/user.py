from sqlalchemy.orm import Session
from jose import  jwt
from datetime import timedelta, datetime
from app.db import models, schema
from app.settings import settings

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schema.User):
    db_user = models.User(username=user.username, password=hash_password(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def hash_password(password):
    return password + "hashingalgorithm"

def verify_password(plain_password, hashed_password):
    return hashed_password == hash_password(plain_password)

def authenticate_user(db: Session, username: str, password: str):
    user = get_user(db, username)
    if not user: 
        return False
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(data: dict, expiry: int, secret: str):
    to_encode = data.copy()
    if expiry:
        expire = datetime.utcnow() + timedelta(minutes=expiry)
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret, algorithm=settings.ALGORITHM)
    return encoded_jwt
    


