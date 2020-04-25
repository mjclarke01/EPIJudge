from test_framework import generic_test


cache = {}

# populate cache
for x in range(256):
    copy_x = x
    ans = 0
    for _ in range(8):
        a = x & 1
        x >>= 1
        ans |= a
        ans <<= 1
    # Need to undo the last shift
    ans >>= 1
    cache[copy_x] = ans


# Version 1 - no cache
# def reverse_bits(x):
#     ans = 0
#     # All numbers are 64 bit
#     for _ in range(64):
#         a = x & 1
#         x >>= 1
#         ans |= a
#         ans <<= 1
#     # Need to undo the last shift
#     ans >>= 1
#
#     return ans


# Version 2 - with a cache
# def reverse_bits(x):
#     mask_size = 8
#     mask = 0b11111111
#     ans = 0
#     # All numbers are 64-bit but the cache contains 8-bit numbers
#     for _ in range(mask_size):
#         a = x & mask
#         x >>= mask_size
#         ans |= cache[a]
#         ans <<= mask_size
#     # Need to undo the last shift
#     ans >>= mask_size
#
#     return ans


# Version 3 - cache but no loop
# Makes no noticeable difference
def reverse_bits(x):
    mask_size = 8
    mask = 0b11111111

    ans = cache[x & mask] << 7 * mask_size
    x >>= mask_size
    ans |= cache[x & mask] << 6 * mask_size
    x >>= mask_size
    ans |= cache[x & mask] << 5 * mask_size
    x >>= mask_size
    ans |= cache[x & mask] << 4 * mask_size
    x >>= mask_size
    ans |= cache[x & mask] << 3 * mask_size
    x >>= mask_size
    ans |= cache[x & mask] << 2 * mask_size
    x >>= mask_size
    ans |= cache[x & mask] << 1 * mask_size
    x >>= mask_size
    ans |= cache[x & mask]

    return ans


# 11001 (25) => 10011 (19)

if __name__ == '__main__':
    print("{0:b}".format(reverse_bits(0b10011101010101100010011000100010110100000)))
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))

