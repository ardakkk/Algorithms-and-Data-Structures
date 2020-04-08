class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0

        for i in range(1, n):
            profit += max(prices[i] - prices[i - 1], 0)
        return profit