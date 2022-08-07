import json
from dataclasses import asdict

import pandas as pd

from scripts.ConfigClasses import Config


class FakeDataGenerator:

    @staticmethod
    def gen_all(spark, tables_class_list, config_path=None):

        # get user config
        if config_path is not None:
            with open(config_path, 'r') as user_config_json:
                user_config_dict = json.load(user_config_json)
        else:
            user_config_dict = {}

        df_list = []
        for table_class in tables_class_list:

            # update table config
            config_dict = {**asdict(table_class.config), **user_config_dict[table_class.__name__]}

            table_class.config = Config.get_from_dict(config_dict)
            table = []
            for _ in range(table_class.config.rows_number):
                obj = table_class()
                table.append(asdict(obj))

            df = spark.createDataFrame(table)
            df_list.append(df)

        return df_list

    @staticmethod
    def gen_joinable(spark, tables_class_list, first_key_list, second_key_list, config_path=None):

        if config_path is not None:
            with open(config_path, 'r') as user_config_json:
                user_config_dict = json.load(user_config_json)
        else:
            user_config_dict = {}

        tables_list = []
        for table_class in tables_class_list:

            config_dict = {**asdict(table_class.config), **user_config_dict}

            table_class.config = Config.get_from_dict(config_dict)
            table = []
            for _ in range(table_class.config.rows_number):
                obj = table_class()
                table.append(obj)

            # df = spark.createDataFrame(table)
            tables_list.append(table)

        # Изменения для джойнов
        for row in range(len(tables_list[0])):
            for col_num in range(len(first_key_list)):
                tables_list[1][row].__dict__[second_key_list[col_num]] = tables_list[0][row].__dict__[
                    first_key_list[col_num]]
        return tables_list

    @staticmethod
    def gen_from_file(spark, table_class, file_path):
        if file_path[-3:] == 'csv':
            file_df = pd.read_csv(file_path)
        else:
            file_df = pd.read_excel(file_path)  # for xlsx require openpyxl

        col_names_csv = file_df.columns.tolist()

        table = pd.DataFrame()
        col_names_dataclass = table_class().__dict__.keys()
        for col_name in col_names_csv:
            if col_name in col_names_dataclass:
                table[col_name] = file_df[col_name]

        return spark.createDataFrame(table)
