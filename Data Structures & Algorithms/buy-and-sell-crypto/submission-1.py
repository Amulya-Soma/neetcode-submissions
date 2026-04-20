class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        mx = 0
        for R in range(len(prices)):
            if prices[L]<prices[R]:
                profit = prices[R]-prices[L]
                mx = max(mx,profit)
            else:
                L = R
        return mx