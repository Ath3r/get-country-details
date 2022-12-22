from fastapi.security import OAuth2PasswordBearer
from app.settings import settings
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=settings.TOKEN_URL)