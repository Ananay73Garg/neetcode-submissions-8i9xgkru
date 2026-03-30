class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = (set(nums))
        b = 0
        c = []
        if a:
            for i in sorted(list(a)):
                if i - 1 in a:
                    b += 1
                else:
                    c.append(b)
                    b = 1
            c.append(b)
            return (max(c))
        else:
            return 0