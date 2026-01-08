# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "postgresql://postgres:sonali123@localhost:5433/report_db"


# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine)

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set in environment variables")

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,   # prevents stale connections
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
