import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# From previous puzzle
def has_cycle(head):
    def get_cycle_len(node):
        count = 1
        start = node
        node = node.next
        while start is not node:
            count += 1
            node = node.next
        return count
    slow = fast = head

    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            l = get_cycle_len(slow)
            slow = head
            fast = head
            for _ in range(l):
                fast = fast.next

            while slow is not fast:
                slow = slow.next
                fast = fast.next

            return slow

    return None


# From previous puzzle
def overlapping_no_cycle_lists(l0, l1):
    def length(node):
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    len_0 = length(l0)
    len_1 = length(l1)
    if len_1 > len_0:
        l0, l1 = l1, l0
    for _ in range(abs(len_0 - len_1)):
        l0 = l0.next

    while l0 and l1 and l0 is not l1:
        l0 = l0.next
        l1 = l1.next

    return l0


def overlapping_lists(l0, l1):
    cycle_l0 = has_cycle(l0)
    cycle_l1 = has_cycle(l1)

    if not cycle_l0 and not cycle_l1:
        return overlapping_no_cycle_lists(l0, l1)
    elif (cycle_l0 and not cycle_l1) or (cycle_l1 and not cycle_l0):
        # Cannot possibly overlap
        return None
    else:
        # # If
        # if l0_cycle is cycle_l1:
        #     return l0_cycle

        # Check for cycles that are not joined
        temp = cycle_l0
        temp = temp.next
        while temp is not cycle_l0:
            if temp is cycle_l1:
                break
            temp = temp.next

        if temp is not cycle_l1:
            return None

        # Check to see if they join before the cycles
        def distance(a, b):
            dist = 0
            while a is not b:
                a = a.next
                dist += 1
            return dist

        stem_l0 = distance(l0, cycle_l0)
        stem_l1 = distance(l1, cycle_l1)
        if stem_l1 > stem_l0:
            l1, l0 = l0, l1
            cycle_l1, cycle_l0 = cycle_l0, cycle_l1
        for _ in range(abs(stem_l0 - stem_l1)):
            l1 = l1.next

        # If they meet in the stems then stop
        # Or if we hit the start of the cycles stop
        while l0 is not l1 and l0 is not cycle_l0 and l1 is not cycle_l1:
            l0 = l0.next
            l1 = l1.next

        return l0 if l0 is l1 else cycle_l0


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("do_lists_overlap.py",
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
