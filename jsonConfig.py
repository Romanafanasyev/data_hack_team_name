import json

class JsonConfig():
    def __init__(self, student_name_len = 15, uni_city_len = 15, age_min = 10, age_max = 20):
        self.student_name_len = student_name_len
        self.uni_city_len = uni_city_len
        self.age_min = age_min
        self.age_max = age_max

    def updateConfig(self, jsonString):
        obj = json.loads(jsonString)
        if 'uni_city_len' in obj:
            self.uni_city_len = obj['uni_city_len']
        if 'student_name_len' in obj:
            self.student_name_len = obj['student_name_len']
        if 'age_min' in obj:
            self.age_min = obj['age_min']
        if 'age_max' in obj:
            self.age_max = obj['age_max']

