from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:
    def __init__(self, capacity):
        self.entries = [None] * capacity
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        if self.tail == len(self.entries):
            self.entries.extend([None] * len(self.entries))

        self.entries[self.tail] = x
        self.tail += 1

    def dequeue(self):
        result = self.entries[self.head]
        self.entries[self.head] = None
        self.head += 1
        if self.head == self.tail:
            self.head = self.tail = 0

        return result

    def size(self):
        print(len(self.entries), self.tail - self.head)
        return self.tail - self.head


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
