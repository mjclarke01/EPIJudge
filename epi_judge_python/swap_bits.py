from test_framework import generic_test


def swap_bits(x, i, j):
    # Get bits at i and j
    xi = (x >> i) & 1
    xj = (x >> j) & 1
    if xi == xj:
        # Do nothing
        return x

    # To toggle on bit i, add 2**i
    # To toggle off bit i, subtract 2**i
    if xi:
        x += 2**j
    else:
        x -= 2**j
    if xj:
        x += 2**i
    else:
        x -= 2**i
    return x


def swap_bits_v2(x, i, j):
    # Get bits at i and j
    xi = (x >> i) & 1
    xj = (x >> j) & 1
    if xi == xj:
        # Do nothing
        return x

    # Create bit mask
    mask = (1 << j) | (1 << i)

    return x ^ mask


# x & (x - 1) clears the lowest set bit
# x & ~(x - 1) clears everything except the lowest set bit

# 01001001 swap 1 and 6 where LSB is rightmost, so 1 is 2nd from the right
# 00001011

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("swap_bits.py", 'swap_bits.tsv',
                                       swap_bits_v2))
