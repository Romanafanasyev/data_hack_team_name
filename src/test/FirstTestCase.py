import os
import unittest
from pyspark.sql import SparkSession
from scripts.fakeDataGenerator import FakeDataGenerator
from test.resource.tables.University import University
from test.resource.tables.Marks import Marks
from test.resource.tables.Student import Student


class FirstTestCase(unittest.TestCase):
    def setUp(self):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.config_path = ROOT_DIR + "/resource/configs/config_1st_test_case.json"
        self.tables_class_list = [Marks, Student, University]
        self.spark = SparkSession.builder.appName("Test").getOrCreate()
        self.df_list = FakeDataGenerator.gen_all(self.spark, self.tables_class_list, config_path=self.config_path)


    def test_df_len(self):
        df = self.df_list[1]
        self.assertEqual(df.count(), 10000, "Wrong len")

    def test_df_max_value(self):
        df = self.df_list[0]
        self.assertEqual(df.filter(df['gpa']>5.0), 0, "Wrong max float")

    def test_df_value_list(self):
        df = self.df_list[0]
        self.assertEqual(df.select('name').distinct().count(), 3, "Doesn't work with list of values")

    def tearDown(self):
        self.spark.close()