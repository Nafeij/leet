"""
    See https://leetcode.com/problems/booking-concert-tickets-in-groups/description/
"""

def comb(x,y):
    return x[0] + y[0], max(x[1],y[1])



class SegTree:
    def __init__(self, ts, fn):
        self.n = len(ts)
        self.t = ([(0,0)]*self.n) + [(ti,ti) for ti in ts]
        self.fn = fn
        self.build()

    def build(self):
        for i in range(self.n - 1, 0, -1):
            self.t[i] = self.fn(self.t[i << 1], self.t[i << 1 | 1])


    def update(self, i, val):
        i += self.n
        self.t[i] = (val,val)
        while i > 1:
            i >>= 1
            self.t[i] = self.fn(self.t[i << 1], self.t[i << 1 | 1])

    def maxQuery(self, k):
        p = 1
        while p < self.n:
            p <<= 1
            if self.t[p][1] < k:
                p += 1
                if self.t[p][1] < k:
                    return -1, -1
        return p - self.n, self.t[p][1]

    def sumQuery(self, r):
        resl, resr = None, None
        l = self.n
        r += self.n + 1
        while l < r:
            if l & 1:
                if resl is None:
                    resl = self.t[l]
                else:
                    resl = self.fn(resl, self.t[l])
                l += 1
            if r & 1:
                r -= 1
                if resr is None:
                    resr = self.t[r]
                else:
                    resr = self.fn(self.t[r], resr)
            l >>= 1
            r >>= 1
        if resl is None:
            return resr
        if resr is None:
            return resl
        return self.fn(resl, resr)

    def fill(self,k,l):
        r = l - 1
        while k > 0:
            r += 1
            s = self.t[r + self.n][0]
            if k < s:
                s -= k
                self.t[r + self.n] = (s, s)
                break
            self.t[r + self.n] = (0, 0)
            k -= s
        self.rebuild(l,r)
        return r
    def rebuild(self, l, r):
        l += self.n
        r += self.n
        while l > 1:
            l >>= 1
            r >>= 1
            for i in range(l,r+1):
                self.t[i] = self.fn(self.t[i << 1], self.t[i << 1 | 1])


class BookMyShow:

    def __init__(self, n: int, m: int):
        self.m = m
        self.seg = SegTree([m]*n, comb)
        self.prev = 0

    def gather(self, k: int, maxRow: int) -> list[int]:
        row, remain = self.seg.maxQuery(k)
        if row > maxRow or row < 0:
            return []
        self.seg.update(row, remain - k)
        return [row, self.m - remain]

    def scatter(self, k: int, maxRow: int) -> bool:
        if self.seg.sumQuery(maxRow)[0] < k:
            return False
        else:
            self.prev = self.seg.fill(k, self.prev)
            return True
