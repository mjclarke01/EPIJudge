from test_framework import generic_test
import functools
import string

num__to_str = {
    0 : "0",
    1 : "1",
    2 : "2",
    3 : "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
}

str_to_num = {
"0" : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}


def convert_base(num_as_string, b1, b2):
    # Convert to base 10
    b10 = 0
    neg = num_as_string[0] == "-"

    # for i in num_as_string:
    #     if i == "-":
    #         neg = True
    #         continue
    #     b10 *= b1
    #     b10 += str_to_num[i]

    b10 = functools.reduce(
        lambda running_sum, c: running_sum * b1 + str_to_num[c],
        num_as_string[neg:], 0
    )

    # Convert to new base
    ans = []
    while True:
        v = b10 % b2
        ans.append(num__to_str[v])
        b10 = b10//b2
        if b10 == 0:
            break

    if neg:
        ans.append("-")

    return ''.join(reversed(ans))


if __name__ == '__main__':
    print(convert_base("615", 7, 13))
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
