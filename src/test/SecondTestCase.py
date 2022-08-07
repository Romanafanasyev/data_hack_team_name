import os
import unittest
from pyspark.sql import SparkSession
from scripts.fakeDataGenerator import FakeDataGenerator
from test.resource.tables.University import University
from test.resource.tables.Marks import Marks
from test.resource.tables.Student import Student

class MyTestCase(unittest.TestCase):
    def setUp(self):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.config_path = ROOT_DIR + "/resource/configs/config_1st_test_case.json"
        self.tables_class_list = [Marks, Student, University]
        self.spark = SparkSession.builder.appName("Test").getOrCreate()
        self.generator = FakeDataGenerator()

    def test_one_col_join(self):
        f_key_list = ['name']
        s_key_list = ['name']
        df_list = self.generator.gen_joinable(self.spark, self.tables_class_list, f_key_list, s_key_list, config_path=self.config_path)
        df1 = df_list[0]
        df2 = df_list[1]
        is_joinable = df1.select('name') == df2.select('name')
        self.assertEqual(is_joinable, True, "Doesn't join")


