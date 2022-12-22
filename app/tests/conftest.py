import pytest

from app.db.models import User

@pytest.fixture(scope="session")
def create_user(tmpdir):
  """Create a user for the tests."""
  from .db_test import override_get_db
  database = next(override_get_db())
  new_user = User()
  database.add(new_user)
  database.commit()
  database.refresh(new_user)
  print("User created")
  yield
  ## Clean up
  # database.query(User).filter_by(username="test").delete()
  # database.commit()