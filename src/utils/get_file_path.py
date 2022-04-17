import sys
import os
import getopt
from typing import List, Tuple, Optional


def show_help() -> None:
    print(
        '''
        This is a simple utility script to clean and prepare data for analysis.
        The basic functions are:
            * Changing and normalizing column names
            * Detecting, changing, and formating data in columns
            * Handling null values
            * Replacing invalid data
        Arguments:
            -h, --help: Instructions on how to run the script.
            -i, --ifile: Path for the input file. The input file should be in csv format.
            -o, --ofile: The name of the output file. The name should end with .csv extension.

            Both input and output file paths should not contain whitespaces.
            For ex:
                -Correct: C:\\Users\\user\Desktop\\prepare_data\\data.csv
                -False: C:\\Users\\user\Desktop\\prepare data\\data.csv
        '''
    )


def get_file_path(argv: List) -> Tuple[str, str]:
    input_file = None
    output_file = None

    try:
        options, arguments = getopt.getopt(argv, 'hi:o:', ['ifile=', 'ofile='])
    except getopt.GetoptError:
        show_help()
        sys.exit(1)

    for opt, arg in options:
        if opt in ['-h', '--help']:
            show_help()
            sys.exit()
        elif opt in ('-i', '--ifile'):
            input_file = check_input_path(arg)
        elif opt in ('-o', '--ofile'):
            output_file = check_output_file(arg)

    return (input_file, output_file)


def check_input_path(path: str) -> Optional[str]:
    if not os.path.isfile(path):
        print('Input file name error. Use -h or --help argument for help.')
        sys.exit(1)
    return os.path.abspath(path)


def check_output_file(path: str) -> Optional[str]:
    if not path.endswith('.csv'):
        print('The extension of the output file should be .csv. Use -h or --help argument for help.')
        sys.exit(1)
    if not os.path.isabs(path):
        return os.getcwd() + '\\' + path
    return os.path.abspath(path)
