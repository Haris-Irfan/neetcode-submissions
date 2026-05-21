class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            min_buy = min(prices[0:i])
            profit = max(prices[i] - min_buy, profit)

        return profit
            