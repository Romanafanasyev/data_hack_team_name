from dataclasses import dataclass
from datetime import datetime


@dataclass
class BasedConfig:
    list_allowed: list = None


@dataclass
class IntConfig(BasedConfig):
    min_int_value: int = 0
    max_int_value: int = 1000000
    mask: str = None


@dataclass
class StrConfig(BasedConfig):
    min_str_len: int = 5
    max_str_len: int = 100
    language: str = "ru_RU"
    str_len: int = None
    mask: str = None


@dataclass
class DatetimeConfig(BasedConfig):
    min_datetime: datetime = datetime(1988, 1, 1)
    max_datetime: datetime = datetime(2030, 12, 31)
    min_timestamp: float = 1659773975.6536
    max_timestamp: float = 1659774975.6536


@dataclass
class FloatConfig(BasedConfig):
    min_float_value: float = -100.0
    max_float_value: float = 100.0


@dataclass
class Config:
    rows_number: int = 10_000
    intConfig: IntConfig = IntConfig()
    strConfig: StrConfig = StrConfig()
    floatConfig: FloatConfig = FloatConfig()
    datetimeConfig: DatetimeConfig = DatetimeConfig()
