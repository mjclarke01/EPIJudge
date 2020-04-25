from test_framework import generic_test
from test_framework.test_failure import TestFailure

int_to_str = {
    0 : "0",
    1 : "1",
    2 : "2",
    3 : "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9"
}

str_to_int = {
    "0" : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}


def int_to_string(x):
    if x == 0:
        return "0"
    ans = []
    neg = False
    if x < 0:
        neg = True
        x *= -1
    while x:
        v = x % 10
        ans.append(int_to_str[v])
        x = x//10

    if neg:
        ans.append("-")

    return "".join(reversed(ans))


def string_to_int(s):
    ans = 0
    for i, c in enumerate(reversed(s)):
        if c == "-":
            ans *= -1
            continue
        ans += str_to_int[c] * (10**i)
    return ans


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
