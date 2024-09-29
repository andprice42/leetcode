class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j = 0
        maxP = 0
        while j < len(prices):
            if j > 0 and prices[j-1] < prices[j]:
                maxP += (prices[j] - prices[j-1])
            j += 1
        return maxP