from test_framework import generic_test
from functools import reduce


def ss_decode_col_id(col):
    total = 0
    for c in col:
        total *= 26
        total += ord(c) - ord("A") + 1
    return total


def ss_decode_col_id(col):
    conv = map(lambda c: ord(c) - ord("A") + 1, col)
    return reduce(lambda result, c: result*26 + c, conv)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
