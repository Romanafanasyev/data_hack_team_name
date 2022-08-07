from typing import ClassVar

from scripts import FieldValueGenerator
from scripts.ConfigClasses import *


@dataclass
class Student:
    config: ClassVar[Config] = Config(
        strConfig=StrConfig(
            max_str_len=20
        )
    )

    id: int = None
    name: str = None
    birth_date: datetime = None

    def __post_init__(self):
        if self.id is None:
            self.id = FieldValueGenerator.generate_int(self.config.intConfig)
            self.name = FieldValueGenerator.generate_str(self.config.strConfig)
            self.birth_date = FieldValueGenerator.generate_datetime(self.config.datetimeConfig)
