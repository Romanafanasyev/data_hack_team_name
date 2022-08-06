import inspect
import sys
import random
import datetime
from faker import Faker
from pandas import DataFrame
import tables
import types
import os.path
from tables.Marks import Marks
from tables.Student import Student
from tables.University import University


class FakeDataGenerator:

    def __init__(self, tables_path):
        self.tables_path = tables_path

    def gen_all(self, config_path=None):
        # load config
        module_names = os.listdir(self.tables_path)
        module_names = [module.replace('.py', '').lower() for module in module_names]
        print(module_names)

        # json_config = JsonConfig()
        # if config_path is not None:
        #     json_config_file = open(config_path, 'r')
        #     config_string = json_config_file.read()
        #     json_config.updateConfig(config_string)

        # df_list - список из всех таблиц, которые сгенерируются
        df_list = []
        for module in module_names:
            clsmembers = inspect.getmembers(sys.modules[module], inspect.isclass)
            class_name = clsmembers[0][0]
            object_dict = clsmembers[0][1].__annotations__

            codemembers = inspect.getmembers(sys.modules[module], inspect.iscode)
            print(codemembers)
            df_name = class_name
            locals()[df_name] = []
            if class_name == 'marks':
                locals()[module] = Marks()
            if class_name == 'student':
                locals()[module] = Student()
            if class_name == 'university':
                locals()[module] = University()
            for col_name in list(object_dict.keys()):
                locals()[col_name] = []
                if col_name == 'config':
                    continue
                locals()[col_name].append()
                print(col_name)
                # for _ in range():

        # for i in range(len(classes_name)):
        #     df_name = classes_name[i]
        #     locals()[df_name] = []
        #     for j in list(object_dict[i].keys()):
        #         locals()[j] = []
                # for l in range(json_config.num_rows):
                #
                #     if object_dict[i][j] == int:
                #         locals()[j].append(random.randint(json_config.min_int_rand, json_config.max_int_rand))
                #     if object_dict[i][j] == float:
                #         locals()[j].append(random.uniform(json_config.min_float_rand, json_config.max_float_rand))
                #     if object_dict[i][j] == str:
                #         locals()[j].append(fake.text().replace(' ', '')[:json_config.txt_length])
                #     if object_dict[i][j] == datetime.datetime:
                #         locals()[j].append(
                #             fake.date_between_dates(date_start=datetime.datetime(json_config.year_start, json_config.month_start, json_config.day_start),
                #                                     date_end=datetime.datetime(json_config.year_end, json_config.month_end, json_config.day_end)))
            #     locals()[df_name].append(locals()[j])
            # locals()[df_name] = DataFrame(locals()[df_name])
            # locals()[df_name] = locals()[df_name].transpose()
            # locals()[df_name].columns = list(object_dict[i].keys())
            # df_list.append(locals()[df_name])
        return df_list

    def gen_one(self, table, config=''):
        pass

    def gen_joinable(self, table1, table2, config=''):
        pass


