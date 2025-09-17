# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        flag = True
        q = deque()
        q.append(root)
        res = []

        while q:
            size = len(q)
            curr = []

            for _ in range(size):
                node = q.popleft()
                curr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if flag == True:
                res.append(curr)
                flag = False
            else:
                res.append(curr[::-1])
                flag = True

        return res
            

            

                





        