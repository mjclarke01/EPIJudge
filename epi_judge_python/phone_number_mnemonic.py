from test_framework import generic_test, test_utils

buttons = {
    "1": ["1"],
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],
    "0": ["0"],
}


def phone_mnemonic(phone_number):
    def _do_it(ans, nums, acc):
        if not nums:
            ans.append(acc)
            return

        for c in buttons[nums[0]]:
            temp = acc + c
            _do_it(ans, nums[1:], temp)

    ans = []
    _do_it(ans, phone_number, "")
    return ans


def phone_mnemonic(phone_number):
    # Non-recursive
    i = 0
    ans = []
    mnem = [""] * len(phone_number)
    tracker = [0] * len(phone_number)

    while True:
        if i < len(phone_number):
            n = phone_number[i]
            if tracker[i] < len(buttons[n]):
                mnem[i] = buttons[n][tracker[i]]
                tracker[i] += 1
                i += 1
            else:
                if i == 0:
                    # Done
                    break

                tracker[i] = 0
                i -= 1
        else:
            ans.append("".join(mnem))
            i -= 1

    return ans


if __name__ == "__main__":
    print(phone_mnemonic("2276696"))
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            "phone_number_mnemonic.tsv",
            phone_mnemonic,
            comparator=test_utils.unordered_compare,
        )
    )
