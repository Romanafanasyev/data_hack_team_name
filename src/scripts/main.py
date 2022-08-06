from pyspark.sql import SparkSession

from scripts.fakeDataGenerator import FakeDataGenerator
from tables.Marks import Marks
from tables.Student import Student
from tables.University import University
import pandas as pd


spark = SparkSession.builder.appName("Test").getOrCreate()
generator = FakeDataGenerator(tables_path='src/tables')

tables_class_list = [Marks, Student]

dataframes_list = generator.gen_all(spark, tables_class_list, config_path='/Users/adalabilbekov/PycharmProjects/pythonProject3/data_hack_team_name/src/userConfig/config.json')
# print(*dataframes_list, sep='\n')

first_key_list = ['id', 'name']
second_key_list = ['id', 'name']
joinable_dataframe_list = generator.gen_joinable(spark, tables_class_list, first_key_list, second_key_list, config_path='/Users/adalabilbekov/PycharmProjects/pythonProject3/data_hack_team_name/src/userConfig/config.json')
# print(*joinable_dataframe_list, sep='\n')

dataframe_from_file = generator.gen_from_file(spark, Student, '/Users/adalabilbekov/PycharmProjects/pythonProject3/data_hack_team_name/src/data_files/student.xlsx')
print(dataframe_from_file)

for i in range(len(dataframes_list)):
    dataframes_list[i] = pd.DataFrame(dataframes_list[i])
print(dataframes_list[0])
print(dataframes_list[1])

for j in range(len(joinable_dataframe_list)):
    joinable_dataframe_list[j] = pd.DataFrame(joinable_dataframe_list[j])
print(joinable_dataframe_list[0])
print(joinable_dataframe_list[1])
