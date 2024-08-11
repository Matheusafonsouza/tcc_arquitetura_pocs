from sqlalchemy import (
    Column,
    MetaData,
    Integer,
    String,
    Text,
    DateTime,
    func,
    create_engine,
)

from ports.database import DatabasePort

metadata = MetaData()


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Define the users table in commonSchema
class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'commonSchema'}
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
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


class PostgresDatabase(DatabasePort):
    def __init__(self, database_uri: str, table: str, schema: str):
        self.table = self.get_table(table)
        engine = create_engine(database_uri)
        self.session = sessionmaker(bind=engine)()

    def get_table(self, table: str):
        return {
            "users": User,
            "books": Book,
            "movies": Movie,
            "tv_shows": TvShow,
        }.get(table)

    def to_dict(self, row: Base):
        print('maia', type(row))
        return {
            field.name: getattr(row, field.name)
            for field in row.__table__.c
        }

    def create(self, data: dict):
        insert = self.table(**data)
        self.session.add(insert)
        self.session.commit()
        return self.to_dict(insert)

    def update(self, id: str, data: dict):
        record = self.session.query(self.table).filter(self.table.id == id).one_or_none()
        if record:
            for key, value in data.items():
                setattr(record, key, value)
            self.session.commit()
            return self.get(record.id)
        return None

    def delete(self, id: str):
        record = self.session.query(self.table).filter(self.table.id == id).one_or_none()
        if record:
            self.session.delete(record)
            self.session.commit()

    def get(self, id: str):
        record = self.session.query(self.table).filter(self.table.id == id).one_or_none()
        if not record:
            return None
        return self.to_dict(record)
