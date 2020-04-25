from test_framework import generic_test


def snake_string(s):
    ans = {
        0: [],
        1: [],
        2: [],
    }

    pattern = [1,0,1,2]
    i = 0
    for c in s:
        ans[pattern[i]].append(c)
        i = i + 1 if i < len(pattern) - 1 else 0

    return ''.join(ans[0]) + ''.join(ans[1]) + ''.join(ans[2])


# Jesus H Christ!
def snake_string(s):
    return s[1::4] + s[0::2] + s[3::4]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("snake_string.py", 'snake_string.tsv',
                                       snake_string))
