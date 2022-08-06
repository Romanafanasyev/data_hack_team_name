from dataclasses import dataclass
from datetime import datetime


@dataclass
class Student:
    id: int
    name: str
    birth_date: datetime
