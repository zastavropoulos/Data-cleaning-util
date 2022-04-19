import os
import sys
from typing import Callable

from .print_data import *


def clear_console() -> None:
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def main_menu_handle() -> None:
    menu_length = main_menu()
    action = get_input(menu_length)
    if action == 1:
        change_column_names()
    elif action == 2:
        format_data()
    elif action == 3:
        handle_null_values()
    elif action == 4:
        handle_invalid_data()
    else:
        sys.exit(0)


def change_column_names() -> None:
    clear_console()
    menu_length = change_column_names_menu()
    action = get_input(menu_length)
    if action == 1:
        pass
    elif action == 2:
        pass
    elif action == 3:
        clear_console()
        main_menu_handle()


def format_data() -> None:
    clear_console()


def handle_null_values() -> None:
    clear_console()


def handle_invalid_data() -> None:
    clear_console()


def get_input(menu_length: int) -> int:
    action = int(input('> '))

    while action > menu_length or action <= 0:
        print('Invalid action.')
        action = int(input('> '))

    return action
