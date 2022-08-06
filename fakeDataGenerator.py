class FakeDataGenerator:

    def __init__(self, path):
        self.path = path

    def gen_all(self, config=''):
        return [['df_1'], ['df_2']]

    def gen_one(self, table, config=''):
        pass

    def gen_joinable(self, table1, table2, config=''):
        pass

    def gnr_test(self, num_rows, min_int_rand, max_int_rand, min_float_rand, max_float_rand,
                 txt_length, year_start, month_start, day_start, year_end, month_end, day_end):

        clsmembers = inspect.getmembers(sys.modules[self.path], inspect.isclass)
        classes_name = []
        object_dict = []
        for i in range(len(clsmembers)):
            classes_name.append(clsmembers[i][0])
            object_dict.append(clsmembers[i][1].__annotations__)

        for i in range(len(classes_name)):
            df_name = classes_name[i]
            locals()[df_name] = []
            for j in list(object_dict[i].keys()):
                locals()[j] = []
                for l in range(num_rows):
                    if object_dict[i][j] == int:
                        locals()[j].append(random.randint(min_int_rand, max_int_rand))
                    if object_dict[i][j] == float:
                        locals()[j].append(random.uniform(min_float_rand, max_float_rand))
                    if object_dict[i][j] == str:
                        locals()[j].append(fake.text().replace(' ', '')[:txt_length])
                    if object_dict[i][j] == datetime.datetime:
                        locals()[j].append(
                            fake.date_between_dates(date_start=datetime.datetime(year_start, month_start, day_start),
                                                    date_end=datetime.datetime(year_end, month_end, day_end)))
                locals()[df_name].append(locals()[j])
            locals()[df_name] = pd.DataFrame(locals()[df_name])
            locals()[df_name] = locals()[df_name].transpose()
            locals()[df_name].columns = list(object_dict[i].keys())
