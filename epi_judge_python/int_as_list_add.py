from test_framework import generic_test
from list_node import ListNode


def add_two_numbers(L1, L2):
    carry = 0
    result = iter = ListNode(0, L1)

    while L1 or L2:
        if not L1 and L2:
            L1, L2 = L2, L1

        if not L1:
            break

        L1.data += L2.data + carry if L2 else carry
        carry, L1.data = divmod(L1.data, 10)

        iter.next = L1
        iter = L1
        L1 = L1.next if L1 and L1.next else None
        L2 = L2.next if L2 and L2.next else None

    if carry:
        iter.next = ListNode(carry)

    return result.next


def add_two_numbers(L1, L2):
    carry = 0
    result = ListNode()
    iter = result

    while L1 or L2 or carry:
        ans = carry
        ans += L1.data if L1 else 0
        ans += L2.data if L2 else 0
        carry = ans // 10

        iter.next = ListNode(ans % 10)
        iter = iter.next
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None

    return result.next






if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_list_add.py",
                                       'int_as_list_add.tsv', add_two_numbers))
