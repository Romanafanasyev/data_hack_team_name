import random
from faker import Faker
from scripts.ConfigClasses import *


def generate_int(intConfig: IntConfig) -> int:
    return random.randint(intConfig.min_int_value, intConfig.max_int_value)


def generate_str(strConfig: StrConfig) -> str:
    return Faker(["ru_RU"]).text().replace(' ', '')[:random.randint(strConfig.min_str_len, strConfig.max_str_len)]


def generate_datetime(datetimeConfig: DatetimeConfig) -> datetime:
    return Faker(['ru_RU']).date_between_dates(datetimeConfig.min_datetime, datetimeConfig.max_datetime)


def generate_float(floatConfig: FloatConfig) -> float:
    return random.uniform(floatConfig.min_float_value, floatConfig.max_float_value)


def generate_timestamp(datetimeConfig: DatetimeConfig) -> float:
    return random.uniform(datetimeConfig.min_timestamp, datetimeConfig.max_timestamp)

