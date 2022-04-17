from string import whitespace
from typing import List


def print_info_as_table(headers: List[str], data: List[List]) -> None:
    columns_width = []
    frame_string = '--'
    header_string = '|'
    # For each column find how wide the column should be.
    # Get the length of each data point and header's name.
    # The width of the column is the max length of the column.
    for j in range(len(data[0])):
        column_sizes = [len(headers[j])]
        for i in range(len(data)):
            column_sizes.append(len(str(data[i][j])))
        columns_width.append(max(column_sizes))
        frame_string += '-' * (columns_width[-1]+1)

    for header in range(len(headers)):
        whitespace = columns_width[header] - len(str(headers[header]))
        header_string += headers[header] + ' ' * whitespace + '|'

    print(frame_string)
    print(header_string)
    print(frame_string)

    for data_row in range(len(data)):
        row_string = '|'
        for data_point in range(len(data[data_row])):
            whitespace = columns_width[data_point] - \
                len(str(data[data_row][data_point]))
            row_string += str(data[data_row][data_point]
                              ) + ' ' * whitespace + '|'
        print(row_string)
        print(frame_string)
