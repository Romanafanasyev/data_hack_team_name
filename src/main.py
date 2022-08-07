import os

from pyspark.sql import SparkSession

from scripts.fakeDataGenerator import FakeDataGenerator
from tables.Marks import Marks
from tables.Student import Student
import pandas as pd


spark = SparkSession.builder.appName("Test").getOrCreate()

tables_class_list = [Marks, Student]

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
config_path = ROOT_DIR + "/userConfig/config.json"

dataframes_list = FakeDataGenerator.gen_all(spark, tables_class_list, config_path=config_path)

# example of tables
print()
for df in dataframes_list:
    df.show()


first_key_list = ['id', 'name']
second_key_list = ['id', 'name']
joinable_dataframe_list = FakeDataGenerator.gen_joinable(
    spark,
    tables_class_list,
    first_key_list,
    second_key_list,
    config_path=config_path)
# print(*joinable_dataframe_list, sep='\n')

xlsx_data_path = ROOT_DIR + "/data_files/student.xlsx"
dataframe_from_file = FakeDataGenerator.gen_from_xlsx(spark, Student, xlsx_data_path)
print(dataframe_from_file)

for i in range(len(dataframes_list)):
    dataframes_list[i] = pd.DataFrame(dataframes_list[i])
print(dataframes_list[0])
print(dataframes_list[1])

for j in range(len(joinable_dataframe_list)):
    joinable_dataframe_list[j] = pd.DataFrame(joinable_dataframe_list[j])
print(joinable_dataframe_list[0])
print(joinable_dataframe_list[1])

spark.close()
