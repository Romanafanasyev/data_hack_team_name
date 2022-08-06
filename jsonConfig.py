import json

class JsonConfig():
    def __init__(self, num_rows = 10000, min_int_rand = 15, max_int_rand = 100, min_float_rand = 1,
                 max_float_rand = 4, txt_length = 10, year_start = 2010, month_start = 1, day_start = 1,
                 year_end = 2022, month_end = 8, day_end = 5):
        self.num_rows = num_rows
        self.min_int_rand = min_int_rand
        self.max_int_rand = max_int_rand
        self.min_float_rand = min_float_rand
        self.max_float_rand = max_float_rand
        self.txt_length = txt_length
        self.year_start = year_start
        self.month_start = month_start
        self.day_start = day_start
        self.year_end = year_end
        self.month_end = month_end
        self.day_end = day_end

    def updateConfig(self, jsonString):
        obj = json.loads(jsonString)
        if 'num_rows' in obj:
            self.num_rows = obj['num_rows']
        if 'min_int_rand' in obj:
            self.min_int_rand = obj['min_int_rand']
        if 'max_int_rand' in obj:
            self.max_int_rand = obj['max_int_rand']
        if 'min_float_rand' in obj:
            self.min_float_rand = obj['min_float_rand']
        if 'max_float_rand' in obj:
            self.max_float_rand = obj['max_float_rand']
        if 'txt_length' in obj:
            self.txt_length = obj['txt_length']
        if 'year_start' in obj:
            self.year_start = obj['year_start']
        if 'month_start' in obj:
            self.month_start = obj['month_start']
        if 'day_start' in obj:
            self.day_start = obj['day_start']
        if 'year_end' in obj:
            self.year_end = obj['year_end']
        if 'month_end' in obj:
            self.month_end = obj['month_end']
        if 'day_end' in obj:
            self.day_end = obj['day_end']

