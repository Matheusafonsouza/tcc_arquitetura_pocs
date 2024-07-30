from domain.entities.movie import Movie
from ports.database import DatabasePort


class MovieRepository:
    def __init__(self, adapter: DatabasePort):
        self.adapter = adapter

    def create(self, data: Movie) -> Movie:
        movie = self.adapter.create(data)
        return Movie(**movie)

    def update(self, id: str, data: Movie) -> Movie:
        movie = self.adapter.update(id, data)
        return Movie(**movie)

    def delete(self, id: str) -> None:
        self.adapter.delete(id)

    def get(self, id: str) -> Movie | None:
        movie = self.adapter.get(id)
        if not movie:
            return None
        return Movie(**movie)
