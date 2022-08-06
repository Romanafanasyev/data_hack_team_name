import random
from faker import Faker
from scripts.ConfigClasses import *


def generate_int(intConfig: IntConfig) -> int:
    if intConfig.list_allowed is not None:
        return random.choice(intConfig.list_allowed)

    return random.randint(intConfig.min_int_value, intConfig.max_int_value)


def generate_str(strConfig: StrConfig) -> str:
    if strConfig.list_allowed is not None:
        return random.choice(strConfig.list_allowed)

    return Faker(["ru_RU"]).text().replace(' ', '')[:random.randint(strConfig.min_str_len, strConfig.max_str_len)]


def generate_datetime(datetimeConfig: DatetimeConfig) -> datetime:
    if datetimeConfig.list_allowed is not None:
        return random.choice(datetimeConfig.list_allowed)

    return Faker(['ru_RU']).date_between_dates(datetimeConfig.min_datetime, datetimeConfig.max_datetime)


def generate_float(floatConfig: FloatConfig) -> float:
    if floatConfig.list_allowed is not None:
        return random.choice(floatConfig.list_allowed)

    return random.uniform(floatConfig.min_float_value, floatConfig.max_float_value)


def generate_timestamp(datetimeConfig: DatetimeConfig) -> float:
    if datetimeConfig.list_allowed is not None:
        return random.choice(datetimeConfig.list_allowed)

    return random.uniform(datetimeConfig.min_timestamp, datetimeConfig.max_timestamp)
