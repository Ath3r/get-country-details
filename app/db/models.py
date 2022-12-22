from .database import Base
from sqlalchemy import Column, String

class User(Base):
    __tablename__ = "users"
    username = Column(String, primary_key=True, index=True)
    password = Column(String)