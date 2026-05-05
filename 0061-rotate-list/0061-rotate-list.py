# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        curr_node = head
        old_tail = curr_node

        while curr_node is not None:
            n += 1
            old_tail = curr_node
            curr_node = curr_node.next

        old_head = head

        if n < 2: # Handling edge cases
            return head

        k = k % n # Making circular linked list

        if k == 0:
            return head

        curr_node = head

        for _ in range(n - k - 1):
            curr_node = curr_node.next

        new_tail = curr_node
        new_head = new_tail.next
        old_tail.next = old_head
        new_tail.next = None

        return new_head