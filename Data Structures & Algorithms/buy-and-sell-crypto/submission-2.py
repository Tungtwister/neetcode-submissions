class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        ans = 0
        for r in range(len(prices)):
            while prices[r] < prices[l]:
                l += 1
            ans = max(prices[r]-prices[l], ans)
        return ans