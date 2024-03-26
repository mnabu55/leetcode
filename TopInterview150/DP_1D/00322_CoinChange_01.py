from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0
        if min(coins) > amount:
            return -1

        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    solution = Solution()

    coins = [1,2,5]
    amount = 11
    expected = 3
    assert solution.coinChange(coins, amount) == expected

    coins = [2]
    amount = 3
    expected = -1
    assert solution.coinChange(coins, amount) == expected

    coins = [1]
    amount = 0
    expected = 0
    assert solution.coinChange(coins, amount) == expected

