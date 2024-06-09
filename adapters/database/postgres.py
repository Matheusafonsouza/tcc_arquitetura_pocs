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
)

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
        operation = insert(self.table).values(**data)
        cursor = self.__connection.execute(operation)
        result = cursor.fetchone()
        return User(**result)
    
    def update(self, id: int, data: dict):
        operation = update(self.table).where(self.table.c.id == id).values(**data)
        cursor = self.__connection.execute(operation)
        result = cursor.fetchone()
        return User(**result)

    def delete(self, id: int):
        operation = delete(self.table).where(self.table.c.id == id)
        cursor = self.__connection.execute(operation)

    def get(self, id: int):
        operation = select(self.table).where(self.table.c.id == id)
        cursor = self.__connection.execute(operation)
        result = cursor.fetchone()
        return User(**result)
