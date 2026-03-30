class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x = []
        for i in range(len(nums)):
            a = 1
            for j in nums[0:i]:
                a*=j
            for j in nums[i+1:len(nums)]:
                a*=j
            x.append(a)

        return x