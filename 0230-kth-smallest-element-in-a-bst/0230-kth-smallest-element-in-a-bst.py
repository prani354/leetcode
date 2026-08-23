# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        heap = []
        def inorder(root):
            if root:
                inorder(root.left)
                heapq.heappush(heap,-root.val)
                if len(heap) > k:
                    heapq.heappop(heap)
                inorder(root.right)

        inorder(root)
        return -heap[0]

         

