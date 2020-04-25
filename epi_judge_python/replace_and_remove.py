import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    # Slow for last test, lots of inserts and removals?
    i = 0
    while True:
        if i < size:
            if s[i] == "a":
                s[i] = "d"
                s.insert(i, "d")
                size += 1
                i += 1
            elif s[i] == "b":
                s.pop(i)
                size -= 1
                continue
            i += 1
        else:
            if i < len(s):
                s.pop(i)
                i += 1
            else:
                break

    return size


def replace_and_remove(size, s):
    # Put "new" values into a new list
    # and then copy them over onto the original
    new_values = []
    for i, v in enumerate(s):
        if i >= size:
            break
        if v == "a":
            new_values.append("d")
            new_values.append("d")
        elif v == "b":
            continue
        else:
            new_values.append(v)

    for i, v in enumerate(new_values):
        if i < len(s):
            s[i] = v
        else:
            s.append(v)

    return len(new_values)


def replace_and_remove(size, s):
    # From the book
    write_idx = 0
    a_count = 0
    for i in range(size):
        if s[i] != "b":
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == "a":
            a_count += 1

    cur_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    while cur_idx >= 0:
        if s[cur_idx] == "a":
            s[write_idx - 1 : write_idx + 1] = "dd"
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1
    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == "__main__":
    print(replace_and_remove(4, ["a", "b", "a", "c", ""]))
    exit(
        generic_test.generic_test_main(
            "replace_and_remove.py",
            "replace_and_remove.tsv",
            replace_and_remove_wrapper,
        )
    )
