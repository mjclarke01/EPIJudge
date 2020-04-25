from test_framework import generic_test
from list_node import ListNode


def even_odd_merge(L):
    # Nothing to do if L has 2 or fewer items
    if not L or not L.next or not L.next.next:
        return L

    dummy = ListNode(0, L)
    dummy_odd = ListNode(0, None)
    even_iter = L
    odd_iter = dummy_odd

    while even_iter.next and even_iter.next.next:
        odd_iter.next = even_iter.next
        even_iter.next = even_iter.next.next

        odd_iter = odd_iter.next
        even_iter = even_iter.next

    # Might be an odd left over
    if even_iter.next:
        odd_iter.next = even_iter.next
        odd_iter = odd_iter.next
    odd_iter.next = None

    even_iter.next = dummy_odd.next

    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_list_merge.py",
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
