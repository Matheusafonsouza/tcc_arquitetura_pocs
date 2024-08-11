from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, DateTime, func
from sqlalchemy.schema import CreateSchema
from sqlalchemy.ext.declarative import declarative_base

# Database configuration
DATABASE_URL = (
    f"postgresql://{environ['PG_USER']}:"
    f"{environ['PG_PASS']}@{environ['PG_HOST']}:"
    f"{environ['PG_PORT']}/{environ['PG_DB']}"
)

# Create an engine
engine = create_engine(DATABASE_URL, echo=True)

# Create schemas
with engine.connect() as conn:
    conn.execute(text('CREATE SCHEMA IF NOT EXISTS "commonSchema"'))
    conn.execute(text('CREATE SCHEMA IF NOT EXISTS "serviceOneSchema"'))
    conn.execute(text('CREATE SCHEMA IF NOT EXISTS "serviceTwoSchema"'))
    conn.execute(text('CREATE SCHEMA IF NOT EXISTS "serviceThreeSchema"'))
    conn.commit()  # Ensure changes are committed

Base = declarative_base()

# Define the users table in commonSchema
class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'commonSchema'}
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

# Define the books table in serviceOneSchema
class Book(Base):
    __tablename__ = 'books'
    __table_args__ = {'schema': 'serviceOneSchema'}
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

class Movie(Base):
    __tablename__ = 'movies'
    __table_args__ = {'schema': 'serviceTwoSchema'}
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

class TvShow(Base):
    __tablename__ = 'tv_shows'
    __table_args__ = {'schema': 'serviceThreeSchema'}
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    episodes = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())
    
# Create the tables
Base.metadata.create_all(engine)
