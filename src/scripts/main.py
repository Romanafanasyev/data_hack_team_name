from scripts.fakeDataGenerator import FakeDataGenerator

generator = FakeDataGenerator(tables_path='/home/roman/PycharmProjects/data_hack_team_name/data_hack_team_name/src/tables')

dataframe_list = generator.gen_all(config_path='../userConfig/config.json')

print(dataframe_list)
print(len(dataframe_list))











