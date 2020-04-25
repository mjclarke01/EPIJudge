from test_framework import generic_test


# Brute force!
def next_permutation(perm):
    i = len(perm) - 1
    glob_to_sort = []

    while i >= 0:
        to_sort = glob_to_sort[:]
        to_sort.append(perm[i])

        for j in range(i - 1, -1, -1):
            # Anything in to_sort which is greater?
            to_sort.sort()
            for ind, g in enumerate(to_sort):
                if g > perm[j]:
                    to_sort[ind], perm[j] = perm[j], to_sort[ind]
                    return perm[0:j + 1] + sorted(to_sort)

            to_sort.append(perm[j])

        glob_to_sort.append(perm[i])
        i -= 1

    return []


# Some help from the book
def next_permutation(perm):
    # Starting from the right find the longest sequence where the order is reversed
    e = len(perm) - 2
    last = perm[-1]
    while e >= 0:
        # if perm[e] == last:
        #     continue
        if perm[e] < last:
            break
        else:
            last = perm[e]
            e -= 1

    if e == -1:
        # Already at the max permutation
        return []

    to_swap = 0
    for i in range(len(perm) - 1, e, -1):
        # Find the lowest number greater than what we want to replace
        if perm[i] > perm[e]:
            to_swap = i
            break

    perm[to_swap], perm[e] = perm[e], perm[to_swap]
    perm[e + 1:] = reversed(perm[e + 1:])
    return perm


if __name__ == "__main__":
    # print(next_permutation([1, 2, 4, 3]))  # 1, 3, 2, 4
    # print(next_permutation([1, 2, 3, 4]))  # 1, 2, 4, 3
    print(next_permutation([4, 3, 2, 1]))  # 4, 3, 2, 1
    # print(next_permutation([3, 4, 2, 1]))  # 4, 3, 2, 1
    # print(next_permutation([1, 3, 5, 4, 2]))  # 1, 4, 2, 3, 5
    # print(next_permutation([8, 6, 15, 18, 17, 10, 17, 13, 16, 1, 6, 1, 18, 11, 1, 12, 15, 6]))
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", "next_permutation.tsv", next_permutation
        )
    )
