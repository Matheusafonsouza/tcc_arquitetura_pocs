from common.repositories.user_repository import UserRepository


def test_create_user(postgres_database):
    user = UserRepository(postgres_database).create({"name": "test"})
    assert user.id
    assert user.name == "test"


def test_delete_user(postgres_database):
    repository = UserRepository(postgres_database)
    created_user = repository.create({"name": "test"})
    repository.delete(created_user.id)
    assert repository.get(created_user.id) is None


def test_update_user(postgres_database):
    repository = UserRepository(postgres_database)
    created_user = repository.create({"name": "test"})
    repository.update(created_user.id, {"name": "test2"})
    updated_user = repository.get(created_user.id)
    assert created_user.id == updated_user.id
    assert created_user.name != updated_user.name
    assert updated_user.name == "test2"


def test_delete_user(postgres_database):
    repository = UserRepository(postgres_database)
    created_user = repository.create({"name": "test"})
    repository.delete(created_user.id)
    updated_user = repository.get(created_user.id)
    assert updated_user is None


def test_get_user(postgres_database):
    repository = UserRepository(postgres_database)
    created_user = repository.create({"name": "test"})
    get_user = repository.get(created_user.id)
    assert created_user.id == get_user.id
    assert created_user.name == get_user.name
