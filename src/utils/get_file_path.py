import sys
import getopt
from typing import List, Tuple


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
            -h: Instructions on how to run the script.
            -i, --ifile: Path for the input file. The input file should be in csv format.
            -o, --ofile: The name of the output file. The name should end with .csv extension.
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
            input_file = arg
        elif opt in ('-o', '--ofile'):
            output_file = arg

    return (input_file, output_file)
