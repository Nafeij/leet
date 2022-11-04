def solution(table):
    res = []
    for r in table:
        res.append(['']*len(table[0]))

    for i in range(len(table)):
        for j in range(len(table[0])):
            o = (i + 1) % 2
            s = 2
            res[o + j * s][i//2] = table[i][j]
    return res



if __name__ == '__main__':
    t = [['a', 'b'],
         ['c', 'd'],
         ['e', 'f'],
         ['g', 'h']]
    sol = solution(t)
    for r in sol:
        print(r)
