from test_framework import generic_test


def is_valid(num):
    if num == "":
        return False
    if int(num) > 255:
        return False
    if len(num) > 1 and num[0] == "0":
        return False
    return True


def is_valid_ip(ip):
    parts = ip.split('.')
    for p in parts:
        if not is_valid(p):
            return False
    return True


def get_valid_ip_address(s):
    if len(s) < 4:
        return []
    if len(s) == 4:
        ip = ".".join([s[0], s[1], s[2], s[3]])
        return [ip] if is_valid_ip(ip) else []
    if len(s) == 12:
        ip = ".".join([s[0:3], s[3:6], s[6:9], s[9:]])
        return [ip] if is_valid_ip(ip) else []
    if len(s) > 12:
        return []

    ans = []
    i, j, k = 1, 2, 3
    while True:
        ip = ".".join([s[0:i], s[i:j], s[j:k], s[k:]])
        if is_valid_ip(ip):
            ans.append(ip)

        if k < len(s) - 1:
            k += 1
        elif j < k -1:
            j += 1
            k = j + 1
        elif i < j - 1:
            i += 1
            j = i + 1
            k = j + 1
            if i > 3:
                # Cannot be valid, so let's bail
                break
        else:
            break

    return ans


# Book version, more or less.
# I added the early checks at the beginning which speed it up significantly
def get_valid_ip_address(s):
    if len(s) < 4:
        return []
    if len(s) == 4:
        ip = ".".join([s[0], s[1], s[2], s[3]])
        return [ip] if is_valid_ip(ip) else []
    if len(s) == 12:
        ip = ".".join([s[0:3], s[3:6], s[6:9], s[9:]])
        return [ip] if is_valid_ip(ip) else []
    if len(s) > 12:
        return []

    ans = []
    for i in range(1, 4):
        if not is_valid(s[0:i]):
            break
        for j in range(i+1, i + 4):
            if not is_valid(s[i:j]):
                break
            for k in range(j + 1, len(s)):
                if not is_valid(s[j:k]):
                    break
                if is_valid(s[j:k]) and is_valid(s[k:]):
                    ans.append(".".join([s[0:i], s[i:j], s[j:k], s[k:]]))
    return ans



def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "valid_ip_addresses.py",
            'valid_ip_addresses.tsv',
            get_valid_ip_address,
            comparator=comp))
