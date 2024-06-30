from os import environ

from adapters.database.sql.postgres import PostgresDatabase
from adapters.database.nosql.mongo import MongoDatabase


def get_postgres_database(table: str) -> PostgresDatabase:
    return PostgresDatabase(
        (
            f"postgresql://{environ["PG_USER"]}:"
            f"{environ["PG_PASS"]}@{environ["PG_HOST"]}:"
            f"{environ["PG_PORT"]}/{environ["PG_NAME"]}"
        ),
        table,
    )


def get_mongo_database(collection: str) -> MongoDatabase:
    return MongoDatabase(
        (
            f"mongodb://{environ["MONGO_USER"]}:"
            f"{environ["MONGO_PASS"]}@{environ["MONGO_HOST"]}:"
            f"{environ["MONGO_PORT"]}"
        ),
        environ["MONGO_COLLECTION"],
        collection,
    )
