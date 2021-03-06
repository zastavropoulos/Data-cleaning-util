from typing import List


def main_menu() -> int:
    choices = ['1. Change column names', '2. Change and format data',
               '3. Handle null values', '4. Handle invalid data', '5. Exit']
    print('\n'.join(choices))

    return len(choices)


def change_column_names_menu() -> int:
    choices = ['1. Change column name', '2. Format column names',
               '3. Back']
    print('\n'.join(choices))
    return len(choices)


def format_names_menu() -> int:
    choices = ['1. Split words with _ (ex. column_name)', '2. Format to lowercase',
               '3. Format to camelCase', '4. Format to PascalCase', '5. Back']
    print('\n'.join(choices))

    return len(choices)


def change_format_data_menu() -> int:
    choices = ['1. Replace value in column', '2. Replace value based on condition',
               '3. Get unique values of a column', '4. Combine two columns',
               '5. Split column', '6. Drop column', '7. Add column based on condition', '8. Back']
    print('\n'.join(choices))

    return len(choices)


def handle_null_values_menu() -> int:
    choices = ['1. Delete all rows with null values', '2. Replace all null values with a value',
               '3. Replace column\'s null values with a value', '4. Back']
    print('\n'.join(choices))

    return len(choices)


def handle_invalid_data_menu() -> None:
    pass


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
