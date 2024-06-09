from adapters.database.sql.postgres import PostgresDatabase
from adapters.database.nosql.mongo import MongoDatabase


def get_postgres_database(table: str) -> PostgresDatabase:
    return PostgresDatabase(
        "postgresql://root:root@postgres:5432/database",
        table,
    )


def get_mongo_database(collection: str) -> MongoDatabase:
    return MongoDatabase(
        "mongodb://root:example@mongo:27017/",
        "database",
        collection,
    )
