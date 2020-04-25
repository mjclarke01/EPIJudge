from test_framework import generic_test


def remove_duplicates(L):
    if L is None:
        return L

    ptr1 = L

    while ptr1:
        ptr2 = ptr1.next
        while ptr2 and ptr2.data == ptr1.data:
            ptr2 = ptr2.next
        ptr1.next = ptr2
        ptr1 = ptr2
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
