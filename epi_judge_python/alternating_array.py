import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName, TestFailure
from test_framework.test_utils import enable_executor_hook


def rearrange(A):
    B = A[:]
    B.sort()
    # interleave
    midpoint = len(A)//2 if len(A) % 2 == 0 else len(A)//2 + 1
    frp = 0
    bp = midpoint
    for i in range(0, len(A)):
        if i % 2 == 0:
            A[i] = B[frp]
            frp += 1
        else:
            A[i] = B[bp]
            bp += 1

    return A

def rearrange(A):
    for i in range(len(A) - 1):
        if i % 2 == 0:
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
        else:
            if A[i] < A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]

    return A

@enable_executor_hook
def rearrange_wrapper(executor, A):
    def check_answer(A):
        for i in range(len(A)):
            if i % 2:
                if A[i] < A[i - 1]:
                    raise TestFailure().with_property(
                        PropertyName.RESULT, A).with_mismatch_info(
                            i, 'A[{}] <= A[{}]'.format(i - 1, i),
                            '{} > {}'.format(A[i - 1], A[i]))
                if i + 1 < len(A):
                    if A[i] < A[i + 1]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                                i, 'A[{}] >= A[{}]'.format(i, i + 1),
                                '{} < {}'.format(A[i], A[i + 1]))
            else:
                if i > 0:
                    if A[i - 1] < A[i]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                                i, 'A[{}] >= A[{}]'.format(i - 1, i),
                                '{} < {}'.format(A[i - 1], A[i]))
                if i + 1 < len(A):
                    if A[i + 1] < A[i]:
                        raise TestFailure().with_property(
                            PropertyName.RESULT, A).with_mismatch_info(
                                i, 'A[{}] <= A[{}]'.format(i, i + 1),
                                '{} > {}'.format(A[i], A[i + 1]))

    executor.run(functools.partial(rearrange, A))
    check_answer(A)


if __name__ == '__main__':
    print(rearrange([1,2,5,3,4]))
    print(rearrange([2,2,3]))

    exit(
        generic_test.generic_test_main("alternating_array.py",
                                       'alternating_array.tsv',
                                       rearrange_wrapper))
