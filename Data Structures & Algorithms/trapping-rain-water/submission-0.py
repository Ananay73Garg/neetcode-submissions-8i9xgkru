class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        res = 0
        while i < len(height) - 1:
            if height[i] <= height[i + 1]:
                i += 1
                res += 0
            else:
                for j in range(i + 1, len(height)):
                    if height[j] >= height[i]:
                        res += (j - i - 1) * height[i] - sum(height[i + 1:j])
                        i = j
                        break
                    if j == len(height) - 1:
                        max_h = max(height[i + 1:])
                        max_index = height.index(max_h, i + 1)
                        res += (max_index - i - 1) * max_h - sum(height[i + 1:max_index])
                        i = max_index
                        break
        return res