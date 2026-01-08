import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Use DATABASE_URL from environment, fallback to local for development
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:sonali123@localhost:5433/report_db"
)

# Fix for SQLAlchemy 2.0+ with PostgreSQL
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)

