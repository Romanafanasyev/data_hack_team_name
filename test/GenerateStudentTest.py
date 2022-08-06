import unittest
from scripts.fakeDataGenerator import FakeDataGenerator


class GenerateAllTablesTest(unittest.TestCase):
    def setUp(self):
        self.generator = FakeDataGenerator('tables')

    def test_student_df_len(self):
        self.assertEqual(len(self.generator.gen_all()[1]['name']), 10000, "Wrong len")

    def test_student_df_with_user_config_len(self):
        self.assertEqual(len(self.generator.gen_all(config_path='/tables/config.json')[1]['name']), 10, "Wrong len")