from common.entities.user import User
from domain.repositories.user_repository import UserRepository


def get_user(user_id: str):
    return UserRepository().get(user_id)


def create_user(data: User):
    return UserRepository().create(data)


def delete_user(user_id: str):
    return UserRepository().delete(user_id)


def update_user(user_id: str, data: User):
    return UserRepository().update(user_id, data)
