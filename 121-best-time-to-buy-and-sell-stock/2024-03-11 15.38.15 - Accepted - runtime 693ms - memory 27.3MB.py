class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        ln = len(prices)
        i = 0
        j = 0
        while i < ln and j < ln:
            delta = prices[j] - prices[i]
            if (delta > maxP):
                maxP = delta
            elif delta < 0:
                i = j
                j = i + 1
            else:
                j += 1
        return maxP