from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    _contents = []
    _max = float("-inf")

    def empty(self):
        return len(self._contents) == 0

    def max(self):
        return self._max

    def pop(self):
        res = self._contents.pop()
        if self._contents:
            self._max = max(self._contents)
        else:
            self._max = float("-inf")
        return res

    def push(self, x):
        self._max = max(x, self._max)
        self._contents.append(x)
        return


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure(
                        "Pop: expected " + str(arg) + ", got " + str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure(
                        "Empty: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported stack operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("stack_with_max.py",
                                       'stack_with_max.tsv', stack_tester))
