import os

from pyspark.sql import SparkSession

from scripts.FakeDataGenerator import FakeDataGenerator
from tables.Marks import Marks
from tables.Student import Student

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
config_path = ROOT_DIR + "/userConfig/config.json"
tables_class_list = [Marks, Student]
spark = SparkSession.builder.appName("Test").getOrCreate()

dataframes_list = FakeDataGenerator.gen_all(spark, tables_class_list, config_path=config_path)
# example of tables
print()
for df in dataframes_list:
    df.show()

csv_data_path = ROOT_DIR + "/data_files/student.csv"
dataframe_from_csv = FakeDataGenerator.gen_from_file(spark, Student, csv_data_path)
dataframe_from_csv.show()

# xlsx_data_path = ROOT_DIR + "/data_files/student.xlsx"
# dataframe_from_xlsx = FakeDataGenerator.gen_from_file(spark, Student, xlsx_data_path)
# dataframe_from_xlsx.show()

first_key_list = ['id', 'name']
second_key_list = ['id', 'name']
joinable_dataframe_list = FakeDataGenerator.gen_joinable(
    spark,
    tables_class_list,
    first_key_list,
    second_key_list,
    config_path=config_path)
# print(*joinable_dataframe_list, sep='\n')

for j in range(len(joinable_dataframe_list)):
    joinable_dataframe_list[j] = pd.DataFrame(joinable_dataframe_list[j])
print(joinable_dataframe_list[0])
print(joinable_dataframe_list[1])

spark.stop()
