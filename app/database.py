
"""
database.py - Database setup

Connects to PostgreSQL and provides a session for each request.
The database URL comes from the DATABASE_URL environment variable
(or a default if not set).
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

from app.logger import get_logger

logger = get_logger(__name__)

# Load any .env file
load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://admin:admin123@localhost:5432/classicmodels",
)

# Create the database connection
try:
    engine = create_engine(DATABASE_URL, echo=False)
    logger.info("Database engine created successfully for: %s", DATABASE_URL.split("@")[-1])
except Exception as e:
    logger.error("Failed to create database engine: %s", str(e))
    raise

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """Get a database session for a request.
    
    FastAPI uses this as a dependency - every endpoint that needs
    database access just asks for 'db' as a parameter.
    """
    db = SessionLocal()
    logger.debug("Database session opened")
    try:
        yield db
    finally:
        db.close()
        logger.debug("Database session closed")
