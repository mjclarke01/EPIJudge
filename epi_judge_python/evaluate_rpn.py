from test_framework import generic_test


def evaluate(expression):
    stack = []
    operators = {
        "/": lambda x, y: x // y,
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
    }

    for t in expression.split(","):
        if len(t) == 1 and t in operators:
            arg2 = stack.pop()
            arg1 = stack.pop()
            stack.append(operators[t](arg1, arg2))
        else:
            stack.append(int(t))

    return stack.pop()


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
