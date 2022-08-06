from dataclasses import asdict
from typing import ClassVar

from scripts import FieldValueGenerator
from scripts.ConfigClasses import *

@dataclass
class Marks:
    config: ClassVar[Config] = Config(
        strConfig=StrConfig(
            max_str_len=20
        )
    )
    id: int = FieldValueGenerator.generate_int(config.intConfig)
    name: str = FieldValueGenerator.generate_str(config.strConfig)
    date: datetime = FieldValueGenerator.generate_datetime(config.datetimeConfig)
    gpa: float = FieldValueGenerator.generate_float(config.floatConfig)

