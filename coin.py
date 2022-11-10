class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [0] + [amount+1] * amount
        for amt in range(1, amount+1):
            for coin in coins:
                if amt >= coin:
                    dp[amt] = min(dp[amt - coin] + 1, dp[amt])
        #print(list(range(0,amount+1)))
        #print(dp)
        return -1 if dp[amount] == amount+1 else dp[amount]


if __name__ == '__main__':
    print(Solution().coinChange([1], 2))
