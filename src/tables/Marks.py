from dataclasses import field

from scripts import FieldValueGenerator
from scripts.ConfigClasses import *

config = Config(
    strConfig=StrConfig(
        max_str_len=20
    )
)


@dataclass
class Marks:
    config: Config = config
    id: int = FieldValueGenerator.generate_int(config.intConfig)
    name: str = FieldValueGenerator.generate_str(config.strConfig)
    date: datetime = FieldValueGenerator.generate_datetime(config.datetimeConfig)
    gpa: float = FieldValueGenerator.generate_float(config.floatConfig)

