import pandas as pd
import sys


class Data_handler():
    def __init__(self, data_path: str) -> None:
        self.data_path = data_path
        try:
            self.df = pd.read_csv(self.data_path)
        except Exception:
            print('Unable to load the data')
            sys.exit(1)

        self.headers = ['Index', 'Column name',
                        'Data type', 'Number of null values']

    def get_general_info(self) -> None:
        print(
            f'\nThe dataset has {self.df.shape[0]} rows and {self.df.shape[1]} columns.\n')

        for i, col in enumerate(self.df.columns.values.tolist(), start=1):
            print(i, col)

    def print_header_frame(self, size_list: list) -> None:
        self.top_string = '--'
        for i in range(len(size_list)):
            self.top_string += '-' * \
                (max(size_list[i], len(self.headers[i]))+1)
        print(self.top_string)

    def print_header_names(self) -> None:
        self.header_string = '|'
        for header in self.headers:
            self.header_string += header + '|'

        print(self.header_string)
