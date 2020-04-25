from test_framework import generic_test

cache = {}


def calc_parity(x):
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


def parity(x):
    mask = 2**8 - 1
    result = 0
    while x:
        # Apply bit mask to first four bits
        masked = x & mask
        x >>= 8
        if masked not in cache:
            # Calculate the parity
            cache[masked] = calc_parity(masked)
        result = 0 if result == cache[masked] else 1
    return result


# 01010000 (80) => 01011111 (95)
def propagate_right(x):
    diff = x ^ (x - 1)
    return x, x ^ (diff >> 1)


def my_mod(num, power):
    mask = power - 1
    return num & mask


def is_power_of_two(num):
    return num & (num - 1) == 0


if __name__ == '__main__':
    print("{0[0]:b} => {0[1]:b}".format(propagate_right(0b01010000)))
    print("{0[0]:b} => {0[1]:b}".format(propagate_right(0b01000100)))

    print(my_mod(77, 64))

    for i in range(2**16):
        if is_power_of_two(i):
            print("{}".format(i))

    # exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
