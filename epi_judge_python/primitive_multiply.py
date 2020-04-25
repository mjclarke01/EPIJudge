from test_framework import generic_test


def multiply(x, y):
    # Start by using long multiplication, may refine later
    ans = 0
    while y:
        if y & 1:
            ans = add(ans, x)
        x <<= 1
        y >>= 1

    return ans


def add(x, y):
    ans = 0
    carry = False
    one = 1
    while x or y:
        if x & 1 and y & 1:
            if carry:
                ans ^= one
            carry = True
        elif x & 1 or y & 1:
            if not carry:
                ans ^= one
        else:
            if carry:
                ans ^= one
            carry = False
        y >>= 1
        x >>= 1
        one <<= 1

    if carry:
        ans ^= one

    return ans


# def add(a, b):
#     while b:
#         carry = a & b
#         a, b = a ^ b, carry << 1
#
#
#     return a


if __name__ == '__main__':
    print("{0:b}".format(multiply(0b1, 0b11)))
    print("{0:b}".format(multiply(0b11, 0b1011)))
    print("{0:b}".format(multiply(0b1011, 0b11)))
    print("{0:b}".format(multiply(57536, 2187)))
    print("{0:b}".format(multiply(2187, 57536)))
    print("{0:b}".format(125831232))
    exit(
        generic_test.generic_test_main("primitive_multiply.py",
                                       'primitive_multiply.tsv', multiply))
