from dataclasses import asdict, dataclass

@dataclass
class Book():
    book_id: int #pk
    title: str
    author_id: int #fk
    price: float
    amount: int

@dataclass
class Author():
    author_id: int#pk
    name_author: str

args_dict = {"price_min": 100.0,
        "price_max": 3000.0,
        "title_len": 10
             }
