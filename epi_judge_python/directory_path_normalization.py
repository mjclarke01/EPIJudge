from test_framework import generic_test


def shortest_equivalent_path(path):
    stack = []

    for p in path.split("/"):
        if p == "..":
            if not stack or stack[~0] == "..":
                stack.append(p)
            else:
                a = stack.pop()
                if a == "":
                    stack.append(p)
        elif p != "." and (p != "" or len(stack) == 0):
            stack.append(p)

    while len(stack) != 0 and stack[~0] == "":
        stack.pop()

    if len(stack) == 0:
        return "/"
    return "/".join(stack)


def shortest_equivalent_path(path):
    stack = []

    if path.startswith("/"):
        stack.append("/")

    for p in path.split("/"):
        if p == "..":
            if not stack or stack[~0] == "..":
                stack.append(p)
            else:
                stack.pop()
        elif p != "." and p != "":
            stack.append(p)

    result = "/".join(stack)
    if result.startswith("//"):
        result = result[1:]

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
