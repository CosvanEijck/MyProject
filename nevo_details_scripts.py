import re


class CSV:
    def __init__(self):
        self.data = "NEVO2021_details.csv"
        self.data_list = []
        self.filtered_list = []
        self.dictionary = {}

    def read_csv_file(self):
        with open(self.data, "r") as opened_file:
            for line in opened_file.readlines():
                line = line.replace("\n", "").split("|")
                self.data_list.append(line)
        return self.data_list

    def filter_csv_list(self, column_label, given_filter):
        for item in self.data_list:
            if re.search(given_filter, item[self.data_list[0].index(column_label)]):
                self.filtered_list.append(item)
        return self.filtered_list

    def create_dictionary(self, value_label, key_label):
        for item in self.filtered_list:
            value = item[self.data_list[0].index(value_label)]
            key = item[self.data_list[0].index(key_label)]
            self.dictionary[key] = int(value)
        return self.dictionary


if __name__ == '__main__':
    c = CSV()
    c.read_csv_file()
    c.filter_csv_list("Eenheid/Unit", "kcal")
    c.create_dictionary("Gehalte/Value", "Voedingsmiddelnaam/Dutch food name")
