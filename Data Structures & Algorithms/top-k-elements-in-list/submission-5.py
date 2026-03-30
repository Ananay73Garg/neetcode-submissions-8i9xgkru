class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        
        for i in nums:
            res[i] = nums.count(i)

        x = dict(sorted(res.items(), key = lambda x : x[1], reverse = True))
        a = list(x.keys())

        b = a[:k]

        return b