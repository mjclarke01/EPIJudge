import copy
import functools
import math

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook

import random

def compute_random_permutation(n):
    b = list(range(n))
    a = []
    for i in range(n):
        n = random.randint(0, len(b) - 1)
        a.append(b.pop(n))
    return a

# From book: it uses the offline sampling algorithm
def compute_random_permutation(n):
    A = list(range(n))
    for i in range(n):
        # Lower bound cannot be 0 as this allows the permutations that have
        # more ways of being achieved becoming more common.
        # Instead use i as the lower bound as it restricts the results to the
        # permutations only, e.g. for n = 3 there are only 6 ways to get the 6 results
        # rather than 27 ways to get 6 results.
        # This is because it stops sequences like the following happening:
        # 1,2,3 => 2,1,3 => 1,2,3
        n = random.randint(i, len(A) - 1)
        A[i], A[n] = A[n], A[i]
    return A


@enable_executor_hook
def compute_random_permutation_wrapper(executor, n):
    def compute_random_permutation_runner(executor, n):
        def permutation_index(perm):
            p = copy.deepcopy(perm)
            idx = 0
            n = len(p)
            while p:
                a = p.pop(0)
                idx += a * math.factorial(n - 1)
                for i, b in enumerate(p):
                    if b > a:
                        p[i] -= 1
                n -= 1
            return idx

        result = executor.run(
            lambda: [compute_random_permutation(n) for _ in range(1000000)])

        return check_sequence_is_uniformly_random(
            [permutation_index(perm)
             for perm in result], math.factorial(n), 0.01)

    run_func_with_retries(
        functools.partial(compute_random_permutation_runner, executor, n))


if __name__ == '__main__':
    # print(compute_random_permutation(2))
    exit(
        generic_test.generic_test_main("random_permutation.py",
                                       'random_permutation.tsv',
                                       compute_random_permutation_wrapper))
