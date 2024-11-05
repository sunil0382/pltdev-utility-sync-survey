from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.settings import settings
from app.models import Customer
from contextlib import contextmanager


postgresql_engine = create_engine(settings.POSTGRESQL_CONNECTION_STRING)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=postgresql_engine)


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def list_customers():
    with get_db() as db_session:
        print("DB Session created")
        try:
            customers = db_session.query(Customer).all()
            print(f"Found {len(customers)} customers")
        except Exception as e:
            print(f"Error executing query: {e}")
