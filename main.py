from faker import Faker
import pandas as pd
import numpy
import random
import inspect
import sys
import datetime
fake = Faker(['ru_RU'])

from dataclasses import dataclass
import datetime


@dataclass
class Student:
    id: int
    name: str
    birth_date: datetime.datetime


@dataclass
class Uni:
    id: int
    city: str
    post_code: str


@dataclass
class Marks:
    id: int
    name: str
    date: datetime.datetime
    gpa: float

import inspect
import sys
clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)

classes_name = []
object_dict = []
for i in range(len(clsmembers)):
    classes_name.append(clsmembers[i][0])
    object_dict.append(clsmembers[i][1].__annotations__)

for i in range(len(classes_name)):
    df_name = classes_name[i]
    locals()[df_name] = []
    for j in list(object_dict[i].keys()):
        locals()[j] = []
        for l in range(10000):
            if object_dict[i][j] == int:
                locals()[j].append(random.randint(18, 100))
            if object_dict[i][j] == float:
                locals()[j].append(random.uniform(10.5, 75.5))
            if object_dict[i][j] == str:
                locals()[j].append(fake.text().replace(' ', '')[:10])
            if object_dict[i][j] == datetime.datetime:
                locals()[j].append(fake.date_between_dates(date_start=datetime.datetime(2010,1,1),
                                                           date_end=datetime.datetime(2022,8,6)))
        locals()[df_name].append(locals()[j])
    locals()[df_name] = pd.DataFrame(locals()[df_name])
    locals()[df_name] = locals()[df_name].transpose()
    locals()[df_name].columns = list(object_dict[i].keys())

print(Uni)

