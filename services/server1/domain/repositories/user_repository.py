from common.entities.user import User
from adapters.database.sql.postgres import PostgresDatabase
from adapters.database.nosql.mongo import MongoDatabase


class UserRepository:
    def __init__(self):
        self.database_adapter = PostgresDatabase(
            "postgresql://root:root@postgres:5432/database",
            "users",
        )
        # self.database_adapter = MongoDatabase(
        #     "mongodb://root:example@mongo:27017/",
        #     "database",
        #     "users",
        # )

    def create(self, data: User) -> User:
        user = self.database_adapter.create(data)
        return User(**user)

    def update(self, id: str, data: User) -> User:
        user = self.database_adapter.update(id, data)
        return User(**user)

    def delete(self, id: str) -> None:
        self.database_adapter.delete(id)

    def get(self, id: str) -> User:
        user = self.database_adapter.get(id)
        if not user:
            return None
        return User(**user)
