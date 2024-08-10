from datetime import datetime

from adapters.database.sql.postgres import User


def test_postgres_database_get_table(postgres_database):
    result = postgres_database.get_table("users")
    assert result == User


def test_postgres_database_create(postgres_database):
    result = postgres_database.create({"name": "test"})
    assert result.get("id") and isinstance(result.get("id"), int)
    assert result.get("created_at") and isinstance(result.get("created_at"), datetime)
    assert result.get("updated_at") and isinstance(result.get("updated_at"), datetime)
    assert result.get("name") == "test"


def test_postgres_database_update(postgres_database):
    user_id = postgres_database.create({"name": "test"}).get("id")
    result = postgres_database.update(user_id, {"name": "test123"})
    assert result.get("id") == user_id
    assert result.get("name") == "test123"


def test_postgres_database_get(postgres_database):
    user_id = postgres_database.create({"name": "test"}).get("id")
    result = postgres_database.get(user_id)
    assert result.get("id") and isinstance(result.get("id"), int)
    assert result.get("id") == user_id
    assert result.get("created_at") and isinstance(result.get("created_at"), datetime)
    assert result.get("updated_at") and isinstance(result.get("updated_at"), datetime)
    assert result.get("name") == "test"


def test_postgres_database_delete(postgres_database):
    user_id = postgres_database.create({"name": "test"}).get("id")
    postgres_database.delete(user_id)
    result = postgres_database.get(user_id)
    assert result == None
