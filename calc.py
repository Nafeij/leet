OPS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}


class Fact:
    def __init__(self, val):
        self.val = val

    def add(self, other):
        return self.opr('+', other)

    def sub(self, other):
        return self.opr('-', other)

    def mul(self, other):
        return self.opr('*', other)

    def div(self, other):
        return self.opr('/', other)

    def opr(self, op, other):
        return Term(op, self, other)

    def solve(self):
        return self


class Lit(Fact):
    def __init__(self, val: int):
        super().__init__(val)

    def __str__(self):
        return str(self.val)


class Var(Fact):
    def __init__(self, val: str):
        super().__init__(val)

    def __str__(self):
        return self.val


class Term(Fact):
    def __init__(self, op: str, left, right):
        super().__init__(op)
        self.left = left
        self.right = right

    def __str__(self):
        return f"({str(self.left)} {self.val} {str(self.right)})"

    def solve(self):
        self.left = self.left.solve()
        self.right = self.right.solve()

        match (self.left, self.right):
            case (Lit(), Lit()):
                return Lit(OPS[self.val](self.left.val, self.right.val))
            case _:
                return self


def test(exp):
    print(exp)
    print("=> " + str(exp.solve()))


if __name__ == '__main__':
    exp = Lit(1).add(Lit(2)).add(Var('x'))
    test(exp)

    exp1 = Lit(5).div(Lit(2)).add(Lit(4).mul(Lit(1).add(Lit(2)).add(Var('x'))))
    test(exp1)

    x, y = Var('x'), Var('y')
    exp2 = y.add(y).sub(y).sub(x.mul(x).div(x).add(y))
    test(exp2)

    exp3 = x.add(Lit(2)).sub(Lit(2)).sub(y).add(y)
    test(exp3)

    exp4 = x.sub(y).add(y)
    test(exp4)

    exp5 = Lit(2).sub(x.add(Lit(2)))
    test(exp5)
