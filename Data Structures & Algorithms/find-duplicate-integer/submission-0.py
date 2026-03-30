class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x = set()
        for i in nums:
            if i not in x:
                x.add(i)
            else:
                return i