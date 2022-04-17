import pandas as pd
import sys

from utils.print_data import *


class Data_handler():
    # TODO: Change the data types and how they look.
    def __init__(self, data_path: str) -> None:
        self.data_path = data_path
        try:
            self.df = pd.read_csv(self.data_path)
        except Exception:
            print('Unable to load the data')
            sys.exit(1)

        self.headers = ['Index', 'Column name',
                        'Data type', 'Number of null values']

        self.get_general_info()

    def get_general_info(self) -> None:
        print(
            f'\nThe dataset has {self.df.shape[0]} rows and {self.df.shape[1]} columns.\n')

        print_info_as_table(self.headers, self.gather_data())

    def gather_data(self) -> List[List]:
        self.data = []

        self.null_counts = self.df.isnull().sum(axis=0).tolist()
        self.dtypes = self.df.dtypes.values.tolist()

        for ind, col in enumerate(self.df.columns.values.tolist(), start=1):
            self.data.extend(
                [[ind, col,  self.dtypes[ind - 1], self.null_counts[ind - 1]]])

        return self.data
