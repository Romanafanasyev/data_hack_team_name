import random
from faker import Faker
from scripts.ConfigClasses import *


def _choice_from_list(config):
    if config.list_allowed_weights is not None:
        return random.choices(config.list_allowed, config.list_allowed_weights)

    return random.choice(config.list_allowed)


def generate_int(intConfig: IntConfig) -> int:
    if intConfig.list_allowed is not None:
        return _choice_from_list(intConfig)

    if intConfig.mask is not None:
        return Faker().lexify(text=intConfig.mask, letters="1234567890")

    return random.randint(intConfig.min_int_value, intConfig.max_int_value)


def generate_str(strConfig: StrConfig) -> str:
    if strConfig.list_allowed is not None:
        return _choice_from_list(strConfig)

    faker = Faker([strConfig.language])

    if strConfig.mask is not None:
        return faker.lexify(text=strConfig.mask)

    # a string of a certain length
    if strConfig.str_len is not None:
        return faker.text().replace(' ', '')[:strConfig.str_len]

    # a string of a random length
    return faker.text().replace(' ', '')[:random.randint(strConfig.min_str_len, strConfig.max_str_len)]


def generate_datetime(datetimeConfig: DatetimeConfig) -> datetime:
    if datetimeConfig.list_allowed is not None:
        return _choice_from_list(datetimeConfig)

    return Faker().date_between_dates(datetimeConfig.min_datetime, datetimeConfig.max_datetime)


def generate_float(floatConfig: FloatConfig) -> float:
    if floatConfig.list_allowed is not None:
        return _choice_from_list(floatConfig)

    return random.uniform(floatConfig.min_float_value, floatConfig.max_float_value)


def generate_timestamp(datetimeConfig: DatetimeConfig) -> float:
    if datetimeConfig.list_allowed is not None:
        return _choice_from_list(datetimeConfig)

    return random.uniform(datetimeConfig.min_timestamp, datetimeConfig.max_timestamp)
