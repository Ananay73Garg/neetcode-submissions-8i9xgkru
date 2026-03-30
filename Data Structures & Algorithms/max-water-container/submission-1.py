class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = []
        for i,n in enumerate(heights):
            for j,k in enumerate(heights):
                res.append(abs(i-j)*min(n,k))
        return max(res)