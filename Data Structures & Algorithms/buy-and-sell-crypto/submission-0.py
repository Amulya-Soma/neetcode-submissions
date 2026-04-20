class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        max1 = 0
        for R in range(len(prices)):
            if prices[L]<prices[R]:
                profit = prices[R]-prices[L]
                max1 = max(profit,max1)
            if prices[L]>prices[R]:
                L = R
        return max1