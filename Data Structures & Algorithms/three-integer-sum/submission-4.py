class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        a = []
        if len(nums) < 2:
            return a
        else:
            for i in range(1,len(nums)-1):
                target = -nums[i]
                j = 0
                k = len(nums)-1
                while j<i and k>i:
                    if (nums[j] + nums[k] < target):
                        j+=1
                    elif (nums[j] + nums[k] > target):
                        k-=1
                    else:
                        a.append([nums[j],nums[i],nums[k]])
                        j+=1
                        k-=1
            x = []
            for d in a:
                if d not in x:
                    x.append(d)
            return x