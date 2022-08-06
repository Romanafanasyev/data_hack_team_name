import unittest
from data_hack_team_name.fakeDataGenerator import FakeDataGenerator


class GenerateAllTablesTest(unittest.TestCase):
    def setUp(self):
        self.generator = FakeDataGenerator('data_hack_team_name.tables')

    def test_student_df_len(self):
        self.assertEqual(len(self.generator.gen_all()[1][1]), 10000, "Wrong len")

    # Почему-то просит абсолютный путь, надо разобраться
    def test_student_df_with_user_config_len(self):
        self.assertEqual(len(self.generator.gen_all(config_path='/home/roman/PycharmProjects/data_hack_team_name/data_hack_team_name/config.json')[1][1]), 10, "Wrong len")