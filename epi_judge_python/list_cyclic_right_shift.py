from test_framework import generic_test
from list_node import ListNode


def cyclically_right_shift_list(L, k):
    if not L:
        return L

    dummy = ListNode(0, L)
    tail = dummy

    length = 0
    while tail.next is not None:
        length += 1
        tail = tail.next

    k = k % length
    if k == 0:
        return L

    new_tail = dummy
    for _ in range(length - k):
        new_tail = new_tail.next

    tail.next = dummy.next
    dummy.next = new_tail.next
    new_tail.next = None

    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("list_cyclic_right_shift.py",
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
