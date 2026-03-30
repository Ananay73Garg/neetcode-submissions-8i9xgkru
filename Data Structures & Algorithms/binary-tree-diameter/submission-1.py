# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.mxpth = 0
        def rec(node):
            if not node:
                return 0
            mleft = rec(node.left)
            mright = rec(node.right)
            self.mxpth = max(self.mxpth, mleft + mright)
            return max(mleft, mright) + 1
        rec(root)
        return self.mxpth

        