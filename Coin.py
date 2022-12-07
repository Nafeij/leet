class Solution:
    '''
        Given list of possible coin denominations and a target amount, find the minimum number of coins
        of all types sufficient to make change
    '''
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [0] + [amount+1] * amount
        for amt in range(1, amount+1):
            for coin in coins:
                if amt >= coin:
                    dp[amt] = min(dp[amt - coin] + 1, dp[amt])
        return -1 if dp[amount] == amount+1 else dp[amount]


if __name__ == '__main__':
    print(Solution().coinChange([1], 3))
