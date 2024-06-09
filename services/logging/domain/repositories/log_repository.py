from domain.entities.log import Log
from adapters.database.nosql.mongo import MongoDatabase


class LogRepository:
    def __init__(self):
        self.database_adapter = MongoDatabase(
            "mongodb://root:example@mongo:27017/",
            "database",
            "logs",
        )

    def create(self, data: Log) -> Log:
        log = self.database_adapter.create(data)
        return Log(**log)
