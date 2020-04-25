from test_framework import generic_test


# def is_palindrome_number(x):
#     # Negative numbers are not palindromes
#     if x < 0:
#         return False
#
#     # Single digit are palindromes
#     if x < 10:
#         return True
#
#     # If last digit is zero then it cannot be a palindrome
#     if x % 10 == 0:
#         return False
#
#     comp = 0
#
#     while True:
#         comp *= 10
#         lsd = x % 10
#         comp += lsd
#
#         # Perhaps length of x was odd then check before removing the digit
#         if comp == x:
#             return True
#
#         # Length of x was even then remove digit and check
#         x //= 10
#         if comp == x:
#             return True
#
#         # Give up
#         if comp > x:
#             break
#
#     return False

def is_palindrome_number(x):
    # Negative numbers are not palindromes
    if x < 0:
        return False

    # Single digit are palindromes
    if x < 10:
        return True

    # If last digit is zero then it cannot be a palindrome
    if x % 10 == 0:
        return False

    # Get number of digits in x
    length = 0
    temp = x

    while temp:
        length += 1
        temp //= 10

    mask = 10 ** (length - 1)

    for _ in range(length // 2):
        if x // mask != x % 10:
            return False
        x %= mask
        x //= 10
        mask //= 100

    return True


if __name__ == '__main__':
    print(is_palindrome_number(123321))
    print(is_palindrome_number(1))
    print(is_palindrome_number(121))
    print(is_palindrome_number(123))
    print(is_palindrome_number(30))
    print(is_palindrome_number(-9))
    print(is_palindrome_number(0))


    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
