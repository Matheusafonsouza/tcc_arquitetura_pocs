from os import environ

from adapters.database.sql.postgres import PostgresDatabase
from adapters.database.nosql.mongo import MongoDatabase


def get_postgres_database(schema: str, table: str) -> PostgresDatabase:
    return PostgresDatabase(
        (
            f"postgresql://{environ['PG_USER']}:"
            f"{environ['PG_PASS']}@{environ['PG_HOST']}:"
            f"{environ['PG_PORT']}/{environ['PG_DB']}"
        ),
        table,
        schema
    )


def get_mongo_database(database: str, collection: str) -> MongoDatabase:
    return MongoDatabase(
        (
            f"mongodb://{environ['MONGO_USER']}:"
            f"{environ['MONGO_PASS']}@{environ['MONGO_HOST']}:"
            f"{environ['MONGO_PORT']}"
        ),
        database,
        collection,
    )
