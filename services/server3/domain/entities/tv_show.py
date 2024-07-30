from datetime import datetime
from dataclasses import dataclass


@dataclass()
class TvShow:
  id: str
  title: str
  year: int
  episodes: int
  created_at: datetime
  updated_at: datetime
