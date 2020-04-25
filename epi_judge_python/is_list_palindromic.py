from test_framework import generic_test


def is_linked_list_a_palindrome(L):
    info = []

    iter = L

    while iter:
        info.append(iter.data)
        iter = iter.next

    if info == [x for x in reversed(info)]:
        return True

    return False


def is_linked_list_a_palindrome(L):
    # make in to a double link list
    info = []

    fwd_iter = L

    while fwd_iter and fwd_iter.next:
        temp = fwd_iter.next
        temp.prev = fwd_iter
        fwd_iter = fwd_iter.next

    back_iter = fwd_iter
    fwd_iter = L

    while fwd_iter is not back_iter and fwd_iter.next is not back_iter:
        if fwd_iter.data != back_iter.data:
            return False
        fwd_iter = fwd_iter.next
        back_iter = back_iter.prev

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
