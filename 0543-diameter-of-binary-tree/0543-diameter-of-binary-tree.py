# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                return 0,0

            left_dia,left_len = dfs(root.left)
            right_dia,right_len = dfs(root.right)

            curr_height = 1 + max(left_len,right_len)
            curr_dia = max(left_dia,right_dia,(left_len+right_len))
            return curr_dia,curr_height

        return dfs(root)[0]