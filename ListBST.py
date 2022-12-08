
plus = lambda x, y : x+y
minus = lambda x, y : x-y
class SegTree:
    def __init__(self, ts, fn):
        self.n = len(ts)
        self.t = (self.n * [0]) + ts
        self.fn = fn
        self.utd = True
        self.build()

    def build(self):
        for i in range(self.n - 1, 0, -1):
            self.t[i] = self.fn(self.t[i << 1], self.t[i << 1 | 1])
        self.utd = True

    def __setitem__(self, item, value):
        if isinstance(item, slice):
            if isinstance(value, int):
                value = [value] * (item.stop-item.start)
            item = slice(item.start + self.n, item.stop + self.n, item.step)
            self.t.__setitem__(item,value)
            self.utd = False
        else:
            item += self.n
            self.t[item] = value
            while item > 1:
                item >>= 1
                self.t[item] = self.fn(self.t[item << 1], self.t[item << 1 | 1])


    def __getitem__(self, item):
        if isinstance(item, slice):
            item = slice(item.start + self.n, item.stop + self.n, item.step)
            return SegTree(self.t[item],self.fn)
        return self.t[item + self.n]

    def query(self, l, r=None):
        if not self.utd:
            self.build()
        if not r:
            r = l+1
        resl, resr = 0, 0
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                resl = self.fn(resl, self.t[l])
                l += 1
            if r & 1:
                r -= 1
                resr = self.fn(self.t[r], resr)
            l >>= 1
            r >>= 1
        return self.fn(resl, resr)


# if __name__ == '__main__':
#     s = SegTree([1,2,3,4])