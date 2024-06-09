from datetime import datetime
from dataclasses import dataclass


@dataclass()
class User:
    id: int
    name: str
    created_at: datetime
    updated_at: datetime
