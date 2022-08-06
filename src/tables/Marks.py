from dataclasses import dataclass
from datetime import datetime


@dataclass
class Marks:
    id: int
    name: str
    date: datetime.datetime
    gpa: float
