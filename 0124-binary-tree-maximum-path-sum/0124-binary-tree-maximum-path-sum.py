# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(u):
            nonlocal ans
            if not u:
                return 0
            l = max(0,dfs(u.left))
            r = max(0,dfs(u.right))
            ans = max(ans,u.val+r+l)
            return u.val + max(l,r)

        ans = float('-inf')
        dfs(root)
        return ans
        