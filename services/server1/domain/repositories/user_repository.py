from common.entities.user import User
from ports.database import DatabasePort


class UserRepository:
    def __init__(self, adapter: DatabasePort):
        self.adapter = adapter

    def create(self, data: User) -> User:
        user = self.adapter.create(data)
        return User(**user)

    def update(self, id: str, data: User) -> User:
        user = self.adapter.update(id, data)
        return User(**user)

    def delete(self, id: str) -> None:
        self.adapter.delete(id)

    def get(self, id: str) -> User:
        user = self.adapter.get(id)
        if not user:
            return None
        return User(**user)
