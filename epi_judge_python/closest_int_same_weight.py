from test_framework import generic_test


def find_first_change(x):
    count = 0

    while x:
        if x & 1 != (x >> 1) & 1:
            return count
        x >>= 1
        count += 1
    raise Exception("Oops!")


def closest_int_same_bit_count(x):
    # Find lowest enabled bit
    lowest = x & ~(x - 1)
    if lowest > 1:
        # If the lowest bit isn't the LSB then we can just swap that bit and
        # the one before
        mask = lowest | (lowest >> 1)
    else:
        # Otherwise, we have to locate the first change in bit value starting
        # from the LSB - is there a quicker way to do this?
        pos = find_first_change(x)
        mask = (1 << pos) | (1 << pos + 1)

    # Swap bits
    ans = x ^ mask

    return ans


if __name__ == '__main__':
    print("{0:b}".format(closest_int_same_bit_count(0b001101)))
    print("{0:b}".format(closest_int_same_bit_count(0b001011)))
    print("{0:b}".format(closest_int_same_bit_count(0b000111)))
    exit(
        generic_test.generic_test_main("closest_int_same_weight.py",
                                       "closest_int_same_weight.tsv",
                                       closest_int_same_bit_count))
