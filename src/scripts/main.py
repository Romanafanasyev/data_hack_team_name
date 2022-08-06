from scripts.fakeDataGenerator import FakeDataGenerator

generator = FakeDataGenerator('tables')

dataframe_list = generator.gen_all(config_path='../userConfig/config.json')

print(dataframe_list)
print(len(dataframe_list))











