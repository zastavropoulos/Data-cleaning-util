import sys
from utils.action_handling import *
from utils.get_file_path import *
from data_handler import *


def main() -> None:
    input_path, output_path = get_file_path(sys.argv[1:])
    d = Data_handler(input_path)
    main_menu_handle(d)


if __name__ == '__main__':
    main()
