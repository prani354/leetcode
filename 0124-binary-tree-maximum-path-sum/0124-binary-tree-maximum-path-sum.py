# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            nonlocal ans

            if not root:
                return 0

            l = max(0,dfs(root.left))
            r = max(0,dfs(root.right))
            ans = max(ans,root.val + l + r)
            return root.val + max(l,r)

        ans = float('-inf')
        dfs(root)
        return ans