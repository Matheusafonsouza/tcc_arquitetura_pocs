from domain.entities.tv_show import TvShow
from ports.database import DatabasePort


class TvShowRepository:
    def __init__(self, adapter: DatabasePort):
        self.adapter = adapter

    def create(self, data: TvShow) -> TvShow:
        tv_show = self.adapter.create(data)
        return TvShow(**tv_show)

    def update(self, id: str, data: TvShow) -> TvShow:
        tv_show = self.adapter.update(id, data)
        return TvShow(**tv_show)

    def delete(self, id: str) -> None:
        self.adapter.delete(id)

    def get(self, id: str) -> TvShow | None:
        tv_show = self.adapter.get(id)
        if not tv_show:
            return None
        return TvShow(**tv_show)
