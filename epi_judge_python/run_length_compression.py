from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s):
    ans = []
    start = 0
    for i, c in enumerate(s):
        if s[i].isdigit():
            continue
        ans.append(int(s[start:i]) * s[i])
        start = i + 1
    return "".join(ans)


def encoding(s):
    ans = ""
    curr = s[0]
    count = 1
    for c in s[1:]:
        if c != curr:
            ans += str(count) + curr
            count = 0
            curr = c
        count += 1

    return ans + str(count) + curr


# From the book - slower than mine!
def encoding(s):
    result = []
    count = 1
    for i in range(1, len(s) + 1):
        if i == len(s) or s[i] != s[i-1]:
            result.append(str(count) + s[i-1])
            count = 1
        else:
            count += 1
    return "".join(result)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure("Decoding failed")
    if encoding(decoded) != encoded:
        raise TestFailure("Encoding failed")


if __name__ == "__main__":
    ans = encoding("aaaabcccaa")
    print(ans)
    print(decoding(ans))
    exit(
        generic_test.generic_test_main(
            "run_length_compression.py", "run_length_compression.tsv", rle_tester
        )
    )
