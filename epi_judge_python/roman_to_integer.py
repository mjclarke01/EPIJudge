from test_framework import generic_test

T = {
    "I": 1,
    # "IV": 4,
    "V": 5,
    # "IX": 9,
    "X": 10,
    # "XL": 40,
    "L": 50,
    # "XC": 90,
    "C": 100,
    # "CD": 400,
    "D": 500,
    # "CM": 900,
    "M": 1000,
    " ": 0,
}


# Version 1 - Exceptions come from dict
# def roman_to_integer(s):
#     ans = 0
#     i = 0
#     while i < len(s):
#         # Look ahead
#         if i < len(s) - 1 and s[i: i+2] in T:
#             ans += T[s[i: i+2]]
#             i += 2
#         else:
#             ans += T[s[i]]
#             i += 1
#
#     return ans


# Version 2 - pure
def roman_to_integer(s):
    ans = 0
    i = 0
    while i < len(s):
        # Look ahead
        first = T[s[i]]
        if i < len(s) - 1 and T[s[i + 1]] > first:
            ans += T[s[i + 1]] - first
            i += 2
        else:
            ans += first
            i += 1

    return ans


# Version 3 - simpler
def roman_to_integer(s):
    ans = T[s[~0]]
    for i in range(len(s) - 1):
        if T[s[i]] < T[s[i + 1]]:
            ans -= T[s[i]]
        else:
            ans += T[s[i]]

    return ans


# Version 4 - reduced version of 3 - less readable?
from functools import reduce


def roman_to_integer(s):
    return reduce(
        lambda val, i: val
        + (-T[s[i]] if T[s[i]] < T[s[i + 1]] else T[s[i]]),
        range(len(s) - 1),
        T[s[~0]]
    )


if __name__ == "__main__":
    print(roman_to_integer("IV"))
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", "roman_to_integer.tsv", roman_to_integer
        )
    )
