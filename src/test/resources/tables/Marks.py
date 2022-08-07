from typing import ClassVar

from scripts import FieldValueGenerator
from scripts.ConfigClasses import *


@dataclass
class Marks:
    config: ClassVar[Config] = Config(
        strConfig=StrConfig(
            max_str_len=20,
            list_allowed=["aaa", 'bbb']
        )
    )

    id: int = None
    name: str = None
    date: datetime = None
    gpa: float = None

    def __post_init__(self):
        if self.id is None:
            self.id = FieldValueGenerator.generate_int(self.config.intConfig)
            self.name = FieldValueGenerator.generate_str(self.config.strConfig)
            self.date = FieldValueGenerator.generate_datetime(self.config.datetimeConfig)
            self.gpa = FieldValueGenerator.generate_float(self.config.floatConfig)
