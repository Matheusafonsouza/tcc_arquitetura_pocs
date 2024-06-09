from domain.repositories.log_repository import LogRepository


def log(message: dict):
    LogRepository().create({"message": message})
