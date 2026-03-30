class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n,m = len(matrix),len(matrix[0])
        l,r = 0,n*m-1
        while l<=r:
            mx = (l+r)//2
            row = mx//m
            col = mx%m

            if matrix[row][col] > target:
                r = mx -1
            elif matrix[row][col] < target:
                l = mx+1
            else:
                return True
        return False
