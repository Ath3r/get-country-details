from app.settings import settings
from sqlalchemy.orm  import sessionmaker
from sqlalchemy import create_engine
from app.main import app
from app.db.database import Base


engine = create_engine(settings.DB_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


