import unittest
from data_hack_team_name.fakeDataGenerator import FakeDataGenerator


class GenerateStudentTest(unittest.TestCase):
    def setUp(self):
        self.generator = FakeDataGenerator('data_hack_team_name/tables.py')

    def test_student_df_len(self):
        self.assertEqual(len(self.generator.gen_all()[0]), 10000, "Wrong len")

