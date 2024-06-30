from sqlalchemy import (
    Table,
    Column,
    MetaData,
    Integer,
    Text,
    DateTime,
    func,
    select,
    insert,
    delete,
    update,
    create_engine,
    literal_column,
)
from uuid import uuid4

from common.entities.user import User
from ports.database import DatabasePort

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", Text, nullable=False),
    Column("created_at", DateTime, nullable=False, server_default=func.now()),
    Column("updated_at", DateTime, nullable=False, server_default=func.now(), onupdate=func.now()),
)


class PostgresDatabase(DatabasePort):
    def __init__(self, database_uri: str, table: str):
        self.table = self.get_table(table)
        engine = create_engine(database_uri)
        self.__connection = engine.connect()

    def get_table(self, table: str):
        return {
            "users": users
        }.get(table)

    def create(self, data: dict):
        operation = insert(self.table).values(**data, id=uuid4()).returning(literal_column("*"))
        cursor = self.__connection.execute(operation)
        self.__connection.commit()
        result = cursor.fetchone()
        return result._mapping
    
    def update(self, id: str, data: dict):
        operation = update(self.table).where(self.table.c.id == id).values(**data)
        self.__connection.execute(operation)
        self.__connection.commit()
        return self.get(id)

    def delete(self, id: str):
        operation = delete(self.table).where(self.table.c.id == id)
        self.__connection.execute(operation)
        self.__connection.commit()

    def get(self, id: str):
        operation = select(self.table).where(self.table.c.id == id)
        cursor = self.__connection.execute(operation)
        result = cursor.fetchone()
        if not result:
            return None
        return result._mapping
