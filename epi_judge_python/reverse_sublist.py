from test_framework import generic_test
from list_node import ListNode


# Could not solve it, this is the book's version
def reverse_sublist(L, start, finish):
    dummy = ListNode(0, L)
    sub_head = dummy

    for _ in range(1, start):
        sub_head = sub_head.next

    sub_head_iter = sub_head.next

    for _ in range(finish - start):
        temp = sub_head_iter.next
        sub_head_iter.next, temp.next, sub_head.next = temp.next,  sub_head.next, temp

    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_sublist.py",
                                       "reverse_sublist.tsv", reverse_sublist))
