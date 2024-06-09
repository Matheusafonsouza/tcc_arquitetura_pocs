from common.entities.user import User
from ports.database import DatabasePort


def get_user(user_id: str, repository: DatabasePort):
    return repository.get(user_id)


def create_user(data: User, repository: DatabasePort):
    return repository.create(data)


def delete_user(user_id: str, repository: DatabasePort):
    return repository.delete(user_id)


def update_user(user_id: str, data: User, repository: DatabasePort):
    return repository.update(user_id, data)
