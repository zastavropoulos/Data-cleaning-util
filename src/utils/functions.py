def get_input(menu_length: int) -> int:
    action = int(input('> '))

    while action > menu_length or action <= 0:
        print('Invalid action.')
        action = int(input('> '))

    return action