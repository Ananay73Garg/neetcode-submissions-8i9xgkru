# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def stringg(root):
            if not root:
                return "x"
            return (str(root.val) + stringg(root.left) + stringg(root.right))
        
        tree = stringg(root)
        subtree = stringg(subRoot)

        return (subtree in tree)