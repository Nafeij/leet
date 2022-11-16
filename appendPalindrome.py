class Solution:
    def matchTable(self, s: str) -> list[int]:
        f = [0] * len(s)
        for i in range(1, len(s)):
            t = f[i - 1]
            while t > 0 and s[i] != s[t]:
                t = f[t - 1]
            if s[i] == s[t]:
                t += 1
            f[i] = t
        return f

    def findAll(self, s: str, w: str) -> list[int]:
        p, t = [], self.matchTable(w)
        i = j = 0
        while i < len(s):
            if w[j] == s[i]:
                i += 1
                j += 1
                if j == len(w):
                    p.append(i - j)
                    j = t[j - 1]
            else:
                if j == 0:
                    i += 1
                else:
                    j = t[j - 1]
        print(len(s))
        return p

    def shortestPalindrome(self, s: str) -> str:
        ns = s + '#' + s[::-1]
        t = self.matchTable(ns)
        return s[:t[-1]-1:-1] + s



if __name__ == '__main__':
    #print(Solution().matchTable("aacecaaa"))
    #print(Solution().findAll("aacecaaa", "c"))
    print(Solution().shortestPalindrome("aacecaaa"))
    print(Solution().shortestPalindrome("abcd"))
