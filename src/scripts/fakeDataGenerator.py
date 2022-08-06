import json
from dataclasses import asdict

from scripts.ConfigClasses import Config


class FakeDataGenerator:

    def __init__(self, tables_path):
        self.tables_path = tables_path

    def gen_all(self, spark, tables_class_list, config_path=None):

        if config_path is not None:
            with open(config_path, 'r') as user_config_json:
                user_config_dict = json.load(user_config_json)
        else:
            user_config_dict = {}

        tables = []
        for table_class in tables_class_list:

            config_dict = asdict(table_class.config) | user_config_dict

            table_class.config = Config.get_from_dict(config_dict)
            table = []
            for _ in range(table_class.config.rows_number):
                obj = table_class()
                table.append((obj,))

            tables.append(table)

        return tables

    def gen_one(self, table, config=''):
        pass

    def gen_joinable(self, table1, table2, config=''):
        pass
