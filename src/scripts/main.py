from pyspark.sql import SparkSession

from scripts.fakeDataGenerator import FakeDataGenerator
from tables.Marks import Marks
from tables.Student import Student
from tables.University import University

obj = Marks()

spark = SparkSession.builder.appName("Test").getOrCreate()
generator = FakeDataGenerator(tables_path='src/tables')

tables_class_list = [Marks, Student, University]
dataframe_list = spark.createDataFrame(
    generator.gen_all(spark, tables_class_list, config_path='src/userConfig/config.json')
)

print(dataframe_list)
print(len(dataframe_list))
