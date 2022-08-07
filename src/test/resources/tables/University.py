from typing import ClassVar

from scripts import FieldValueGenerator
from scripts.ConfigClasses import *


@dataclass
class University:
    config: ClassVar[Config] = Config(
        strConfig=StrConfig(
            max_str_len=20
        )
    )
    id: int = None
    uni_name: str = None
    avg_exam_score: float = None

    def __post_init__(self):
        if self.id is None:
            self.id = FieldValueGenerator.generate_int(self.config.intConfig)
            self.name = FieldValueGenerator.generate_str(self.config.strConfig)
            self.avg_exam_score = FieldValueGenerator.generate_float(self.config.floatConfig)
