from datetime import datetime
from dataclasses import dataclass


@dataclass()
class Movie:
  id: str
  title: str
  year: int
  created_at: datetime
  updated_at: datetime
