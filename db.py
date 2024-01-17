import os
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine

load_dotenv()


# engine object created to connect with database
engine = create_async_engine(url=os.getenv("DATABASE_URL"), echo=True)

# object is createed for model creation
# Base = DeclarativeBase()


# Class can also be  created for models creation, both work in the same way
class Base(DeclarativeBase):
    pass
