from test_framework import generic_test

cache = {1: "1"}


def look_and_say(n):
    if n == 1:
        ans = cache[1]
    else:
        ans = cache[n-1]
        temp = ""
        count = 0
        last = None
        for c in ans:
            if not last:
                last = c
                count = 1
            elif c != last:
                temp += str(count)
                temp += last
                last = c
                count = 1
            else:
                count += 1
        temp += str(count)
        temp += last
        ans = temp
        cache[n] = ans

    return ans


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "look_and_say.py", "look_and_say.tsv", look_and_say
        )
    )
