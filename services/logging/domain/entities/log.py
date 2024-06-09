from datetime import datetime
from dataclasses import dataclass


@dataclass()
class Log:
    id: str
    message: str
    created_at: datetime
    updated_at: datetime
