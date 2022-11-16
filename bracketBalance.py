MATCH = {'{': '}', '[': ']', '(': ')'}


def isBalanced(st):
    stack = []
    for c in st:
        if c in MATCH:
            stack.append(c)
        else:
            if not stack or MATCH[stack.pop()] != c:
                return False
    return not stack


if __name__ == '__main__':
    tests = [["()[]{}", True],
             ["([)]", False],
             ["{{[](}})", False],
             ["{[()]}", True]]

    for t in tests:
        assert isBalanced(t[0]) == t[1]
