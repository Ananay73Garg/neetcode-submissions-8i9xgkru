class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        x = {}
        y= {}
        for i,n in enumerate(numbers):
            x[n] = i
            y[target-n] = i

        for t in x.keys():
            if t in y.keys():
                return [x[t]+1,y[t]+1]
                break