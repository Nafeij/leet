from itertools import accumulate


class Solution:
    def manachers(self, s: str):
        pSize = [0] * len(s)
        c = rb = 0
        for i in range(len(s)):
            mirror = 2 * c - i  # c - (i - c)
            if i < rb:
                pSize[i] = min(rb - i, pSize[mirror])  # skip to lowerbound
            l = 1 + pSize[i]
            while i + l < len(s) and i - l >= 0 and s[i + l] == s[i - l]:
                l += 1
                pSize[i] += 1
            if i + pSize[i] > rb:
                c = i
                rb = i + pSize[i]
        return pSize

    def helper(self, man: list[int]):
        n = len(man)
        ints = [(i - man[i], i + man[i]) for i in range(n)]
        arr = [0] * n
        for a, b in ints:
            arr[b] = max(arr[b], b - a + 1)
        for i in range(n - 2, -1, -1):
            arr[i] = max(arr[i], arr[i + 1] - 2)
        return list(accumulate(arr, max))

    def maxProduct(self, s: str):
        m = self.manachers(s)
        t1, t2 = self.helper(m), self.helper(m[::-1])[::-1][1:] + [0]
        #print(t1)
        return max(x * y for x, y in zip(t1, t2))

    def maxProduct1(self, s: str):
        man = self.manachers(s)
        n = len(man)
        lefts, rights = [0] * n, [0] * n
        for i, l in enumerate(man):
            tl = 2*l + 1
            lefts[i - l] = max(tl, lefts[i - l])
            rights[i + l] = max(tl, rights[i + l])
        for i in range(1, n):
            lefts[i] = max(lefts[i], lefts[i - 1] - 2)
        for i in range(n - 2, -1, -1):
            rights[i] = max(rights[i], rights[i + 1] - 2)
            lefts[i] = max(lefts[i], lefts[i+1])
        for i in range(1, n):
            rights[i] = max(rights[i], rights[i-1])
        return max(x * y for x, y in zip(lefts[1:] + [0], rights))


if __name__ == '__main__':
    sol = Solution()
    t = "ggbswiymmlevedhkbdhntnhdbkhdevelmmyiwsbgg"
    m = sol.manachers(t)
    print(' ' + ', '.join(t))
    print(m)
    # print(sol.maxProduct("ggbswiymmlevedhkbdhntnhdbkhdevelmmyiwsbgg"))
    print(sol.maxProduct(t))
    print(sol.maxProduct1(t))
