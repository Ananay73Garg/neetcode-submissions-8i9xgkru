class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = []
        if len(prices) == 1:
            return 0
        else:
            for i,n in enumerate(prices):
                for j in range(i+1,len(prices)):
                    if prices[j] >= n:
                        res.append((prices[j]-n))
                    else:
                        res.append(0)
            return max(res)