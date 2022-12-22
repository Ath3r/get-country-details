from fastapi import APIRouter

from app.api.v1 import user
from app.api.v1 import details

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(details.router, prefix="/details", tags=["details"])