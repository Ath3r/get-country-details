from fastapi import APIRouter, Depends, HTTPException, status
from app.auth.oauth import oauth2_scheme
from app.service.jwt import verify_token
from sqlalchemy.orm import Session
from app.db.dep import get_db
from app.service.details import get_country_details

router = APIRouter()

@router.post("/get-phone-country")
async def get_phone_country(phone: str, token = Depends(oauth2_scheme), db: Session = Depends(get_db)): 
    verify_token(db,token)
    return get_country_details(phone)