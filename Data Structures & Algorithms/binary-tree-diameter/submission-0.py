# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    mxpth = 0
    def rec(self,root):
        if not root:
            return 0

        mleft = self.rec(root.left)
        mright = self.rec(root.right)

        self.mxpth = max(self.mxpth,mleft+mright)

        return max(mleft,mright) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.rec(root.left)
        right = self.rec(root.right)

        return max(self.mxpth,left+right)

        