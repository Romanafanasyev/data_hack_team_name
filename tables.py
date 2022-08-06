from dataclasses import dataclass
import datetime


@dataclass
class Student:
    id: int
    name: str
    birth_date: datetime.datetime


@dataclass
class Uni:
    id: int
    city: str
    post_code: str


@dataclass
class Marks:
    id: int
    name: str
    date: datetime.datetime
    gpa: float