import random as r


def solution(n, m, queries):
    rs = [1 for _ in range(n)]
    cs = [1 for _ in range(m)]
    mr = mc = 0

    def next(s, l):
        for i in range(s, len(l)):
            if l[i] == 1:
                return i
        return -1

    ans = []

    for q in queries:
        if q[0] == 0:
            min = -1
            if mr != -1 and mc != -1:
                min = (mr + 1) * (mc + 1)
            ans.append(min)
        elif q[0] == 1:
            rs[q[1] - 1] = 0
            mr = next(mr, rs)
        elif q[0] == 2:
            cs[q[1] - 1] = 0
            mc = next(mc, cs)
    return ans


if __name__ == '__main__':
    n = 100
    m = 100
    # queries = [[0], [1, 2], [0], [2, 1], [0], [1, 1], [0]]
    queries = [[0]]
    for _ in range(1000):
        queries.append([r.randint(1, 2), r.randint(1, 100)])
        queries.append([0])
    print(solution(n, m, queries))
