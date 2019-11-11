# Time: O(n) | Space: O(1)
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        max_profit = 0
        cheapest_price = prices[0]

        for price in prices:
            cheapest_price = min(price, cheapest_price)
            current_profit = price - cheapest_price
            max_profit = max(max_profit, current_profit)

        return max_profit