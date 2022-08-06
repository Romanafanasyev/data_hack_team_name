import json
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class IntConfig:
    min_int_value: int = 0
    max_int_value: int = 1000000
    list_allowed: list = None


@dataclass
class StrConfig:
    min_str_len: int = 5
    max_str_len: int = 100
    list_allowed: list = None


@dataclass
class DatetimeConfig:
    min_datetime: datetime = datetime(1988, 1, 1)
    max_datetime: datetime = datetime(2030, 12, 31)
    list_allowed: list = None


@dataclass
class FloatConfig:
    min_float_value: float = -100.0
    max_float_value: float = 100.0
    list_allowed: list = None


@dataclass
class Config:
    rows_number: int = 10_000
    intConfig: IntConfig = IntConfig()
    strConfig: StrConfig = StrConfig()
    floatConfig: FloatConfig = FloatConfig()
    datetimeConfig: DatetimeConfig = DatetimeConfig()


print(json.dumps(asdict(Config()), default=str))
