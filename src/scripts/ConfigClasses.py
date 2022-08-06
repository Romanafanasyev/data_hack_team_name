from dataclasses import dataclass
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
    min_timestamp: float = 1659773975.6536
    max_timestamp: float = 1659774975.6536
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
