import sys
from utils.get_file_path import *


def main() -> None:
    input_path, output_path = get_file_path(sys.argv[1:])


if __name__ == '__main__':
    main()
