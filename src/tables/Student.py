from scripts import FieldValueGenerator
from scripts.ConfigClasses import *

config = Config(
    strConfig=StrConfig(
        max_str_len=20
    )
)


@dataclass
class Student:
    id: int = FieldValueGenerator.generate_int(config.intConfig)
    name: str = FieldValueGenerator.generate_str(config.strConfig)
    birth_date: datetime = FieldValueGenerator
