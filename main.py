from data_hack_team_name.fakeDataGenerator import FakeDataGenerator
import tables

generator = FakeDataGenerator('tables')

dataframe_list = generator.gen_all(config_path='config.json')

print(dataframe_list)











