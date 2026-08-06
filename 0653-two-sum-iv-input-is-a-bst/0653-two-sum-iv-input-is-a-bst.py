# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        vals = {}

        def func(node):
            if not node:
                return False

            if node.val in vals:
                return True
            
            vals[k-node.val] = True

            return func(node.left) or func(node.right)

        return func(root)
            