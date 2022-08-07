import os
import unittest
from pyspark.sql import SparkSession
from scripts.FakeDataGenerator import FakeDataGenerator
from resources.tables.Marks import Marks


class FirstTestCase(unittest.TestCase):

    root_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = root_dir + "/resources/configs/config_1st_test_case.json"
    tables_class_list = [Marks]
    spark = SparkSession.builder.appName("Test").getOrCreate()
    df_list = FakeDataGenerator.gen_all(spark, tables_class_list, config_path=config_path)

    def test_df_len(self):
        df = self.df_list[0]
        self.assertEqual(df.count(), 10, "Wrong len")

    def test_df_max_value(self):
        df = self.df_list[0]
        self.assertEqual(df.filter(df['gpa'] > 5.0).count(), 0, "Wrong max float")

    def test_df_value_list(self):
        df = self.df_list[0]
        self.assertEqual(df.select('name').distinct().count(), 3, "Doesn't work with list of values")
