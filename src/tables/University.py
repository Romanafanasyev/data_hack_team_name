from typing import ClassVar

from scripts import FieldValueGenerator
from scripts.ConfigClasses import *


@dataclass
class University:
    config: ClassVar[Config] = Config(
        rows_number=100,
        intConfig=IntConfig(
            min_int_value=150,
            max_int_value=200
        )
    )
    id: int = FieldValueGenerator.generate_int(config.intConfig)
    city: str = FieldValueGenerator.generate_str(config.strConfig)
    post_code: str = FieldValueGenerator.generate_str(config.strConfig)
