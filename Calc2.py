OPS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}


class Exp:
    def __init__(self, val):
        self.val = val

    def Add(self, other):
        return self.opr('+', other)

    def Sub(self, other):
        return self.opr('-', other)

    def Mul(self, other):
        return self.opr('*', other)

    def opr(self, op, other):
        return Term(op, self, other)

    def simplify(self):
        return self


class Lit(Exp):
    def toString(self):
        return str(self.val)


class Var(Exp):
    def toString(self):
        return self.val


class Term(Exp):
    def __init__(self, op: str, left, right):
        super().__init__(op)
        self.left = left
        self.right = right

    def toString(self):
        return f"({self.left.toString()} {self.val} {self.right.toString()})"

    def simplify(self):
        left = self.left.simplify()
        right = self.right.simplify()
        match (left, right):
            case (Lit(), Lit()):
                return Lit(OPS[self.val](left.val, right.val))
            case _:
                return Term(self.val, left, right)


def test(exp):
    print(exp)
    print("=> " + str(exp.simplify()))


if __name__ == '__main__':
    e = Lit(1).Add(Lit(2)).Add(Lit(3))
    print(e.toString())
    print(e.simplify().toString())
    print(e.toString())
