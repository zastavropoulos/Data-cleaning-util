import os
import sys

from data_handler import Data_handler
from .print_data import *
from .string_manipulation import *
from .formating_data import *
from .functions import get_input


# TODO: When choosing column to change name give the ability to go back.


def clear_console() -> None:
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def main_menu_handle(data_handler: Data_handler) -> None:
    menu_length = main_menu()
    action = get_input(menu_length)
    if action == 1:
        change_column_names(data_handler)
    elif action == 2:
        format_data(data_handler)
    elif action == 3:
        handle_null_values(data_handler)
    elif action == 4:
        handle_invalid_data()
    else:
        sys.exit(0)


def change_column_names(data_handler: Data_handler) -> None:
    clear_console()
    menu_length = change_column_names_menu()
    action = get_input(menu_length)
    if action == 1:
        change_column_name(data_handler)
    elif action == 2:
        format_column_names(data_handler)
    elif action == 3:
        clear_console()
        main_menu_handle(data_handler)


def format_data(data_handler: Data_handler) -> None:
    clear_console()
    menu_length = change_format_data_menu()
    action = get_input(menu_length)

    if action == 1:
        print('Replace value in column')
    elif action == 2:
        print('Replace value based on condition')
    elif action == 3:
        clear_console()
        get_column_unique_values(data_handler)
        format_data(data_handler)
    elif action == 4:
        print('Combine two columns')
    elif action == 5:
        print('Split column')
    elif action == 6:
        clear_console()
        drop_column(data_handler)
        format_data(data_handler)
    elif action == 7:
        print('Add column based on condition')
    else:
        clear_console()
        main_menu_handle(data_handler)


def handle_null_values(data_handler: Data_handler) -> None:
    clear_console()
    menu_length = handle_null_values_menu()
    action = get_input(menu_length)
    if action == 1:
        data_handler.get_df().dropna(inplace=True)
        handle_null_values(data_handler)
    elif action == 2:
        value = str(input('Value to replace > '))
        data_handler.get_df().fillna(value, inplace=True)
        handle_null_values(data_handler)
    elif action == 3:
        print('Choose column to replace null values')
        column_names = data_handler.get_column_names()
        for ind, col in column_names:
            print(f'{ind}. {col}')
        column_index = get_input(len(column_names)) - 1
        replace_value = str(input('Replace value > '))
        column_name = column_names[column_index][1]
        data_handler.get_df()[column_name].fillna(replace_value, inplace=True)
        handle_null_values(data_handler)
    else:
        clear_console()
        main_menu_handle(data_handler)


def handle_invalid_data() -> None:
    clear_console()


def change_column_name(data_handler: Data_handler) -> None:
    clear_console()
    print('Choose column to alter name')
    column_names = data_handler.get_column_names()
    for ind, col in column_names:
        print(f'{ind}. {col}')
    column_index = get_input(len(column_names)) - 1
    new_name = str(input('New name > '))
    old_name = str(column_names[column_index][1])
    data_handler.get_df().rename(columns={old_name: new_name}, inplace=True)
    other_change = str(input('Would you like to change something else?(y/n) '))
    if other_change == 'y':
        change_column_name(data_handler)
    change_column_names(data_handler)


def format_column_names(data_handler: Data_handler) -> None:
    clear_console()
    menu_length = format_names_menu()
    action = get_input(menu_length)
    if action == 1:
        new_names = split_data(data_handler.get_df().columns.values)
        data_handler.get_df().columns = new_names
        format_column_names(data_handler)
    elif action == 2:
        new_names = format_lowercase(data_handler.get_df().columns.values)
        data_handler.get_df().columns = new_names
        format_column_names(data_handler)
    elif action == 3:
        new_names = format_camelCase(data_handler.get_df().columns.values)
        data_handler.get_df().columns = new_names
        format_column_names(data_handler)
    elif action == 4:
        new_names = format_PascalCase(data_handler.get_df().columns.values)
        data_handler.get_df().columns = new_names
        print(data_handler.get_df().columns)
        format_column_names(data_handler)
    else:
        change_column_names(data_handler)
