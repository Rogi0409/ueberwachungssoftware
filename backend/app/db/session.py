from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os

Database_url = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/ueberwachungssoftware",)

engine = create_engine(Database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()