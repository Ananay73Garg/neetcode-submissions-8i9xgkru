class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def btime(x):
            return sum([math.ceil(p/x) for p in piles])

        l = 1
        r = max(piles)
        res = r

        while l<=r:
            m = (l+r)//2

            if btime(m) <= h:
                res = m
                r = m-1
            else:
                l = m+1

        return res