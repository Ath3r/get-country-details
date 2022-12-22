import pytest

from app.db.models import User

@pytest.fixture(scope="session", autouse=True)
def create_user():
  """Create a user for the tests."""
  from .db_test import override_get_db
  database = next(override_get_db())
  new_user = User(username="test", password="test")
  database.add(new_user)
  database.commit()
  database.refresh(new_user)
  yield
  ## Clean up
  database.query(User).filter_by(username="test").delete()
  database.commit()