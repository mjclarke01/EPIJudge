from test_framework import generic_test


def examine_buildings_with_sunset(buildings):
    stack = []

    for i in range(len(buildings) - 1, -1, -1):
        if len(stack) == 0:
            stack.append(i)
        else:
            if buildings[i] > buildings[stack[~0]]:
                stack.append(i)

    return stack


# This is from the book, it assumes that the list of buildings are some kind of
# generator rather than a big array, so uses less space
def examine_buildings_with_sunset(buildings):
    stack = []

    for i, b in enumerate(buildings):
        while stack and b >= stack[~0][1]:
            stack.pop()
        stack.append((i, b))

    return [x[0] for x in reversed(stack)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "sunset_view.py", "sunset_view.tsv", examine_buildings_with_sunset
        )
    )
