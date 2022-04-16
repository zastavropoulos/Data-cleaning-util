import sys
from utils.get_file_path import *
from data_handler import *


def main() -> None:
    input_path, output_path = get_file_path(sys.argv[1:])
    d = Data_handler(input_path)
    d.print_header_frame([1, 1, 1, 1])
    d.print_header_names()
    d.print_header_frame([1, 1, 1, 1])


if __name__ == '__main__':
    main()
