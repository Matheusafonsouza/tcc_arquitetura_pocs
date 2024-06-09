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
    id = postgres_database.create({"name": "test"}).id
    result = postgres_database.update(id, {"name": "test123"})
    assert result.id and isinstance(result.id, str)
    assert result.created_at and isinstance(result.created_at, datetime)
    assert result.updated_at and isinstance(result.updated_at, datetime)
    assert result.name == "test123"


def test_postgres_database_get(postgres_database):
    id = postgres_database.create({"name": "test"}).id
    result = postgres_database.get(id)
    assert result.id and isinstance(result.id, str)
    assert result.id == id
    assert result.created_at and isinstance(result.created_at, datetime)
    assert result.updated_at and isinstance(result.updated_at, datetime)
    assert result.name == "test"


def test_postgres_database_get(postgres_database):
    id = postgres_database.create({"name": "test"}).id
    postgres_database.delete(id)
    result = postgres_database.get(id)
    assert result == None
