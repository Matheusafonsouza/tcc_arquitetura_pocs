from datetime import datetime

from adapters.database.sql.postgres import users


def test_postgres_database_get_table(postgres_database):
    result = postgres_database.get_table("users")
    assert result == users


def test_postgres_database_create(postgres_database):
    result = postgres_database.create({"name": "test"})
    assert result.id and isinstance(result.id, str)
    assert result.created_at and isinstance(result.created_at, datetime)
    assert result.updated_at and isinstance(result.updated_at, datetime)
    assert result.name == "test"


def test_postgres_database_update(postgres_database):
    user_id = postgres_database.create({"name": "test"}).id
    result = postgres_database.update(user_id, {"name": "test123"})
    assert result.id and isinstance(result.id, str)
    assert result.created_at and isinstance(result.created_at, datetime)
    assert result.updated_at and isinstance(result.updated_at, datetime)
    assert result.name == "test123"


def test_postgres_database_get(postgres_database):
    user_id = postgres_database.create({"name": "test"}).id
    result = postgres_database.get(user_id)
    assert result.id and isinstance(result.id, str)
    assert result.id == user_id
    assert result.created_at and isinstance(result.created_at, datetime)
    assert result.updated_at and isinstance(result.updated_at, datetime)
    assert result.name == "test"


def test_postgres_database_get(postgres_database):
    user_id = postgres_database.create({"name": "test"}).id
    postgres_database.delete(user_id)
    result = postgres_database.get(user_id)
    assert result == None
