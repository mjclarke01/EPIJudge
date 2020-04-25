from test_framework import generic_test


def power(x, y):
    if y == 0:
        return 1

    if y == 1:
        return x

    if x == 0:
        return 0

    if y < 0:
        y = -y
        x = 1 / x

    ans = 1

    while y:
        if y & 1:
            ans *= x
        x *= x
        y >>= 1
    return ans



if __name__ == '__main__':
    print(power(2, 0))
    print(power(2, 2))
    print(power(2, 3))
    print(power(-1.0006612108596369, -2217))
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
