from test_framework import generic_test


def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1

    return True


def is_palindrome(s):
    sanitised = [x.lower() for x in s if x.isalnum()]

    for i, j, k in zip(range(len(s)), sanitised, reversed(sanitised)):
        if i > len(sanitised) / 2:
            break

        if j != k:
            return False

    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
