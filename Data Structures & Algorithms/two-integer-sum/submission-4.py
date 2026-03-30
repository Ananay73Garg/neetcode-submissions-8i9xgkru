class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tag = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in tag:
                return [tag[diff],i]
            tag[n] = i