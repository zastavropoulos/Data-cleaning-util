from typing import List

possible_word_delimiters = [' ', '_', '/', '|', '-', '.', ';']


def split_data(columns: List[str]) -> List[str]:
    new_column_names = columns

    for i in range(len(new_column_names)):
        for delimiter in possible_word_delimiters:
            if delimiter in new_column_names[i]:
                new_column_names[i] = '_'.join(
                    new_column_names[i].split(delimiter))
    return new_column_names


def format_lowercase(columns: List[str]) -> List[str]:
    return [column.lower() for column in columns]


def format_camelCase(columns: List[str]) -> List[str]:
    # TODO: Too cryptic I think, probably needs revision.
    new_column_names = columns

    for i in range(len(new_column_names)):
        for delimiter in possible_word_delimiters:
            if delimiter in new_column_names[i]:
                splited = new_column_names[i].split(delimiter)
                splited = [splited[0]] + [w.title() for w in splited[1:]]
                new_column_names[i] = delimiter.join(splited)

    return new_column_names


def format_PascalCase(columns: List[str]) -> List[str]:
    return [c.title() for c in columns]
