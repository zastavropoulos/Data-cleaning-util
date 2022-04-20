from data_handler import Data_handler

from .functions import get_input


def drop_column(data_handler: Data_handler) -> None:
    columns = data_handler.get_column_names()
    print('Choose a column to drop.')
    for ind, col in columns:
        print(f'{ind}. {col}')
    df = data_handler.get_df()
    action = get_input(len(columns)) - 1
    df.drop(df.columns[[action]], axis=1, inplace=True)


def get_column_unique_values(data_handler: Data_handler) -> None:
    columns = data_handler.get_column_names()
    print('Choose a column to drop.')
    for ind, col in columns:
        print(f'{ind}. {col}')
    df = data_handler.get_df()
    action = get_input(len(columns)) - 1
    unique_values = df[columns[action][1]].unique()
    print(
        f'The column {columns[action][1]} has {len(unique_values)} unique values.')
    print('\n'.join([str(i) for i in unique_values]))
    input('Press a button to continue > ')
