from test_framework import generic_test


def generate_pascal_triangle(n):
    result = []

    for i in range(n):
        if i == 0:
            result.append([1])
            continue
        prev_row = result[i - 1]
        next_row = [1]
        for j in range(len(prev_row) - 1):
            next_row.append(prev_row[j] + prev_row[j + 1])
        next_row.append(1)
        result.append(next_row)

    return result


# Based on the book
def generate_pascal_triangle(n):
    # Pre-allocate space by filling with ones
    result = [[1] * (i + 1) for i in range(n)]

    for i in range(n):
        if i == 0:
            continue
        prev_row = result[i - 1]

        for j in range(1, i):
            result[i][j] = prev_row[j - 1] + prev_row[j]
    return result


if __name__ == "__main__":
    generate_pascal_triangle(4)
    exit(
        generic_test.generic_test_main(
            "pascal_triangle.py", "pascal_triangle.tsv", generate_pascal_triangle
        )
    )
