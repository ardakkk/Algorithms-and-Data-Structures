# Time: O(A * C) Where A is amount, c is number of coins | Space: O(A) We created a DP array of length A
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp_min_coins = [float("inf")] * (amount + 1)
        dp_min_coins[0] = 0

        for i in range(1, len(dp_min_coins)):
            amount = i
            for coin_value in coins:
                if coin_value <= amount:
                    dp_min_coins[i] = min(dp_min_coins[amount - coin_value] + 1, dp_min_coins[i])

        answer = dp_min_coins[-1]

        if answer == float("inf"):
            return -1

        return answer
