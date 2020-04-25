from test_framework import generic_test


def is_well_formed(s):
    pairs = {
        "{": "}",
        "[": "]",
        "(": ")",
    }

    stack = []
    for c in s:
        if c in pairs:
            stack.append(c)
        elif not stack or c != pairs[stack.pop()]:
            return False

    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
