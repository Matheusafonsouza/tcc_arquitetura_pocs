from domain.entities.book import Book
from ports.database import DatabasePort


class BookRepository:
    def __init__(self, adapter: DatabasePort):
        self.adapter = adapter

    def create(self, data: Book) -> Book:
        print("ADAPTER ADAPTER ADAPTER ADPTER")
        book = self.adapter.create(data)
        return Book(**book)

    def update(self, id: str, data: Book) -> Book:
        book = self.adapter.update(id, data)
        return Book(**book)

    def delete(self, id: str) -> None:
        self.adapter.delete(id)

    def get(self, id: str) -> Book | None:
        book = self.adapter.get(id)
        if not book:
            return None
        return Book(**book)
