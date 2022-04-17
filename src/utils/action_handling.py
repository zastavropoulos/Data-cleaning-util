import os


def clear_console() -> None:
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def change_column_names(data_handler) -> None:
    clear_console()
    print('1. Change column name')
    print('2. Format column names')
    print('3. Back')

    action = int(input('> '))

    while action > 3 or action <= 0:
        change_column_names(data_handler)

    if action == 1:
        pass
    elif action == 2:
        pass
    else:
        clear_console()
        data_handler.get_general_info()


def format_data() -> None:
    clear_console()


def handle_null_values() -> None:
    clear_console()


def handle_invalid_data() -> None:
    clear_console()
