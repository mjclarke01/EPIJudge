from test_framework import generic_test


# def multiply(num1, num2):
#     first = True
#     neg = False
#
#     if num2[0] < 0:
#         neg = not neg
#         num2[0] *= -1
#
#     if num1[0] < 0:
#         neg = not neg
#         num1[0] *= -1
#
#     if (len(num1) == 1 and num1[0] == 0) or len(num2) == 1 and num2[0] == 0:
#         return [0]
#
#     ans = [0] * (len(num1) + len(num2))
#
#     for i in reversed(num2):
#         if first:
#             first = False
#         else:
#             num1.append(0)
#
#         if i == 0:
#             continue
#
#         index = len(ans) - 1
#
#         # Use carry to try to avoid some by index look-ups
#         # which can be slower
#         carry = 0
#
#         for j in reversed(num1):
#             val = ans[index] + carry + j * i
#             if val > 9:
#                 carry = val // 10
#                 ans[index] = val % 10
#             else:
#                 ans[index] = val
#                 carry = 0
#
#             index -= 1
#         ans[index] += carry
#
#     if ans[0] == 0:
#         ans.pop(0)
#
#     if neg:
#         ans[0] *= -1
#
#     return ans

# Is faster if we sort the 'carry' out afterwards
def multiply(num1, num2):
    first = True
    neg = False

    if num2[0] < 0:
        neg = not neg
        num2[0] *= -1

    if num1[0] < 0:
        neg = not neg
        num1[0] *= -1

    if (len(num1) == 1 and num1[0] == 0) or len(num2) == 1 and num2[0] == 0:
        return [0]

    ans = [0] * (len(num1) + len(num2))

    for i in reversed(num2):
        if first:
            first = False
        else:
            num1.append(0)

        if i == 0:
            continue

        index = len(ans) - 1

        for j in reversed(num1):
            ans[index] += j * i
            index -= 1

    for i in reversed(range(len(ans))):
        if ans[i] > 9:
            ans[i - 1] += ans[i] // 10
            ans[i] %= 10

    if ans[0] == 0:
        ans.pop(0)

    if neg:
        ans[0] *= -1

    return ans

# Textbook answer - actually slower!
# Slower because using 'for i in reversed(num1)' is quicker than
# 'for i in reversed(range(len(num1)))'
# Looking up a value by index takes time
# def multiply(num1, num2):
#
#     # sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
#     # num1[0], num2[0] = abs(num1[0]), abs(num2[0])
#
#     sign = 1
#
#     if num2[0] < 0:
#         sign *= -1
#         num2[0] *= -1
#
#     if num1[0] < 0:
#         sign *= -1
#         num1[0] *= -1
#
#     if (len(num1) == 1 and num1[0] == 0) or len(num2) == 1 and num2[0] == 0:
#         return [0]
#
#     result = [0] * (len(num1) + len(num2))
#     for i in reversed(range(len(num1))):
#         for j in reversed(range(len(num2))):
#             result[i + j + 1] += num1[i] * num2[j]
#             result[i + j] += result[i + j + 1] // 10
#             result[i + j + 1] %= 10
#
#     # Remove the leading zeroes.
#     # result = result[next((
#     #     i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
#     if result[0] == 0:
#         result.pop(0)
#
#     if sign == -1:
#         result[0] = result[0] * sign
#     return result
#     # return [sign * result[0]] + result[1:]

if __name__ == '__main__':
    # print(multiply([1, 2, 3], [2]))  # 2 4 6
    # print(multiply([1, 2, 9], [6]))  # 7 7 4
    # print(multiply([1, 2, 9], [9]))  # 1 1 6 1
    # print(multiply([1, 2, 3], [2, 0]))  # 2 4 6 0
    # print(multiply([1, 2, 3], [2, 0, 0]))  # 2 4 6 0 0
    # print(multiply([1, 2, 3], [2, 0, 1]))  # 2 4 7 2 3
    # print(multiply([-1, 2, 3], [-2, 0, 1]))  # 2 4 7 2 3
    print(multiply([-9, 8, 5], [6, 8, 8]))  # 6 7 7 6 8 0
    print(multiply([1, 9, 3, 7, 0, 7, 7, 2, 1], [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]))  # -1 4 7 5 7 3 9 5 2 5 8 9 6 7 6 4 1 2 9 2 7

    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
