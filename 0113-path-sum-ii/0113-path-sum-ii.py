# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        
        def dfs(root,targetSum,temp,res):
            if not root:
                return

            temp.append(root.val)

            if not root.left and not root.right and sum(temp) == targetSum:
                res.append(temp[:])

            dfs(root.left,targetSum,temp,res)
            dfs(root.right,targetSum,temp,res)

            temp.pop()
        res = []
        dfs(root,targetSum,[],res)

        return res


