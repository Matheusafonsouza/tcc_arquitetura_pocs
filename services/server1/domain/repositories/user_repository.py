from common.entities.user import User
from adapters.database.postgres import PostgresDatabase


class UserRepository:
    def __init__(self):
        self.database_adapter = PostgresDatabase(
            "postgresql://root:root@postgres:5432/database",
            "users",
        )

    def create(self, data: User) -> User:
        return self.database_adapter.create(data)

    def update(self, id: int, data: User) -> User:
        return self.database_adapter.update(id, data)

    def delete(self, id: int) -> None:
        self.database_adapter.delete(id)

    def get(self, id: int) -> User:
        return self.database_adapter.get(id)
