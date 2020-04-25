from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n):
    # Sieve of Eratosthenes
    result = []
    not_primes = set()

    for i in range(2, n + 1):
        if i not in not_primes:
            result.append(i)
            val = i + i
            while val <= n + 1:
                not_primes.add(val)
                val += i

    return result


if __name__ == "__main__":
    print(generate_primes(18))
    exit(
        generic_test.generic_test_main(
            "prime_sieve.py", "prime_sieve.tsv", generate_primes
        )
    )
