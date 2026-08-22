# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def height(root):
            if not root:
                return 0

            left_tree = height(root.left)
            right_tree = height(root.right)

            if abs(left_tree - right_tree) > 1:
                balanced[0] = False
                return 0

            return 1 + max(left_tree,right_tree)

        height(root)
        return balanced[0]

        