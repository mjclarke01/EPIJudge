from test_framework import generic_test


# Super slow brute force
# def divide(x, y):
#     if y == 1:
#         return x
#
#     count = 0
#     while x >= y:
#         x -= y
#         count += 1
#
#     return count

def divide(x, y):
    ans = 0

    while x >= y:
        k = 0
        temp = y << k
        while temp << 1 <= x:
            k += 1
            temp = y << k

        ans += 1 << k
        x -= temp

    return ans


def pretty_print(x, y):
    print("{0:b} ({0}) / {1:b} ({1}) = {2:b} ({2})".format(x, y,
        divide(x, y)))


if __name__ == '__main__':
    # pretty_print(0b1000000, 0b1)
    # pretty_print(0b100, 0b10)
    # pretty_print(0b110, 0b11)
    # pretty_print(0b111, 0b10)
    pretty_print(0b1110101, 0b1001)

    pretty_print(16, 3)

    exit(
        generic_test.generic_test_main("primitive_divide.py",
                                       "primitive_divide.tsv", divide))
