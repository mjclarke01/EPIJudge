from test_framework import generic_test
from test_framework.test_failure import TestFailure
from collections import deque


class QueueWithMax:
    main_q = []
    dirty = True
    max_val = float("-inf")

    def enqueue(self, x):
        if x > self.max_val:
            self.max_val = x
            self.dirty = False

        self.main_q.append(x)

    def dequeue(self):
        result = self.main_q.pop(0)
        if result == self.max_val:
            self.dirty = True
        return result

    def max(self):
        if self.dirty:
            self.max_val = max(self.main_q)
            self.dirty = False
        return self.max_val

class QueueWithMax:
    main_q = []
    max_deq = deque()

    def enqueue(self, x):
        while self.max_deq and x > self.max_deq[~0]:
            self.max_deq.pop()
        self.max_deq.append(x)

        self.main_q.append(x)

    def dequeue(self):
        result = self.main_q.pop(0)
        if result == self.max_deq[0]:
            self.max_deq.popleft()
        return result

    def max(self):
        return self.max_deq[0]


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_with_max.py",
                                       'queue_with_max.tsv', queue_tester))
