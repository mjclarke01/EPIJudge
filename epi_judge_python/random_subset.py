import functools

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    binomial_coefficient, check_sequence_is_uniformly_random,
    compute_combination_idx, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook
from random import randint


def random_subset(n, k):
    # Uses unnecessary space when k << n
    a = [i for i in range(n)]
    for i in range(k):
        r = randint(i, n - 1)
        a[i], a[r] = a[r], a[i]
    return a[:k]


def random_subset(n, k):
    # Hash table containing only the changes
    changes = {}
    for i in range(k):
        r = randint(i, n - 1)
        changes[i], changes[r] = changes.get(r, r), changes.get(i, i)
    return [changes[i] for i in range(k)]


@enable_executor_hook
def random_subset_wrapper(executor, n, k):
    def random_subset_runner(executor, n, k):
        results = executor.run(
            lambda: [random_subset(n, k) for _ in range(100000)])

        total_possible_outcomes = binomial_coefficient(n, k)
        comb_to_idx = {
            tuple(compute_combination_idx(list(range(n)), n, k, i)): i
            for i in range(binomial_coefficient(n, k))
        }
        return check_sequence_is_uniformly_random(
            [comb_to_idx.get(tuple(sorted(result)), 0)
             for result in results], total_possible_outcomes, 0.01)

    run_func_with_retries(
        functools.partial(random_subset_runner, executor, n, k))


if __name__ == '__main__':
    random_subset(100, 4)
    exit(
        generic_test.generic_test_main("random_subset.py", 'random_subset.tsv',
                                       random_subset_wrapper))
