# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        if not root:
            return False
        
        # Queue stores tuples of (current_node, parent_node)
        queue = deque([(root, None)])
        
        while queue:
            level_size = len(queue)
            x_parent = None
            y_parent = None
            
            # Process all nodes at the current depth
            for _ in range(level_size):
                node, parent = queue.popleft()
                
                # Record the parent if we find x or y
                if node.val == x:
                    x_parent = parent
                elif node.val == y:
                    y_parent = parent
                
                # Add children to the queue with 'node' as their parent
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            
            # After finishing the current level, evaluate findings:
            # 1. Both found at the same depth -> check if parents are different
            if x_parent and y_parent:
                return x_parent != y_parent
            
            # 2. Only one found at this depth -> they are at different depths
            if x_parent or y_parent:
                return False
                
        return False