import random as r

'''
    Given m, m, implying an n*m grid where grid[i][j] = (i+1)*(j+1) and all elements have an 'activated' state,
        , and a list of queries [(t,i,j),...],
    process the queries sequentially:
    1. If t == 0
        Find the minimum element among the activated element and append it to a list to be returned
    2. If t == 1
        Deactivate elements in row i
    3. If t == 2
        Deactivate elements in column i
'''


def solution(n, m, queries):
    rs = [1 for _ in range(n)]
    cs = [1 for _ in range(m)]
    mr = mc = 1

    def next(s, ls):
        for i in range(s-1, len(ls)):
            if ls[i]:
                return i + 1
        return 0

    ans = []

    for q in queries:
        if q[0] == 0:
            minn = -1
            if mr and mc:
                minn = mr * mc
            ans.append(minn)
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
    queries = [[0], [1, 2], [0], [2, 1], [0], [1, 1], [0]]
    # queries = [[0]]
    # for _ in range(1000):
    #     queries.append([r.randint(1, 2), r.randint(1, 100)])
    #     queries.append([0])
    print(solution(n, m, queries))
