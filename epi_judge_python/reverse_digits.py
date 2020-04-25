from test_framework import generic_test


def reverse(x):
    is_neg = x < 0
    if is_neg:
        x *= -1
    ans = 0

    while x:
        ans *= 10
        ans += x % 10
        x //= 10

    if is_neg:
        ans *= -1

    return ans


if __name__ == '__main__':
    print(reverse(-314))
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
