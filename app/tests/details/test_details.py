import pytest
from httpx import AsyncClient

from app.service.user import  create_access_token, authenticate_user
from app.tests.db_test import app
from app.settings import settings


@pytest.mark.asyncio
async def test_get_phone_country():
  """Test get phone country."""
  async with AsyncClient(app=app, base_url="http://test") as ac:
    user_access_token = create_access_token(data={"sub": "test"}, expiry=settings.ACCESS_TOKEN_EXPIRE_MINUTES,secret=settings.SECRET)
    response = await ac.post("/api/v1/details/get-phone-country", headers={"Authorization": f"Bearer {user_access_token}"},params={"phone": "+919999999999"})
    assert response.json() == {"country": "IN", "phone": "+919999999999"}
    assert response.status_code == 200
