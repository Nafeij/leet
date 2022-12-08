class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        runProfit = 0
        min = prices[0]
        for p in prices:
            if p < min:
                min = p
            elif p - min > runProfit:
                runProfit = p - min
        return runProfit