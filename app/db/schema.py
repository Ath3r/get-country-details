from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    password: str

class UserCreate(UserBase):
    password: str

class User(UserCreate):
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str = None