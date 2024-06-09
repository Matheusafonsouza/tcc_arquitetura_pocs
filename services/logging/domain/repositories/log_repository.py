from domain.entities.log import Log
from ports.database import DatabasePort


class LogRepository:
    def __init__(self, adapter: DatabasePort):
        self.adapter = adapter

    def create(self, data: Log) -> Log:
        log = self.adapter.create(data)
        return Log(**log)
