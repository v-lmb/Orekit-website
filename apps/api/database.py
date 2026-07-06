import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from dotenv import load_dotenv

# Reads the .env file and retrieves the connection URL
load_dotenv()
DATABASE_URL = os.environ["DATABASE_URL"]

# Connection engine
engine = create_engine(DATABASE_URL)

# Create sessions
SessionLocal = sessionmaker(bind=engine)


# Parent class of all SQLAlchemy models
class Base(DeclarativeBase):
    pass
