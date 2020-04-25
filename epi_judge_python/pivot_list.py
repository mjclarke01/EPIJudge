import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from list_node import ListNode


def list_pivoting(l, x):
    # Pivot around the supplied value, lower go first, higher go last
    # Must maintain relative order
    # Hint: do the three regions independently
    first = ListNode()
    first_iter = first
    second = ListNode()
    second_iter = second
    third = ListNode()
    third_iter = third

    while l is not None:
        if l.data < x:
            first_iter.next = l
            first_iter = first_iter.next
        elif l.data == x:
            second_iter.next = l
            second_iter = second_iter.next
        elif l.data > x:
            third_iter.next = l
            third_iter = third_iter.next
        else:
            raise Exception("WTF!")
        l = l.next

    third_iter.next = None
    # Order is important in case second is empty
    second_iter.next = third.next
    first_iter.next = second.next

    return first.next


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pivot_list.py", 'pivot_list.tsv',
                                       list_pivoting_wrapper))
