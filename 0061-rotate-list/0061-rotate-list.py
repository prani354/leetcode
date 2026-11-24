# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None
        curr = head
        l = 1
        
        while curr.next:
            curr = curr.next
            l += 1

        k = k % l
        curr.next = head
        res = head

        for _ in range(l-k-1):
            res = res.next

        temp = res.next
        res.next = None

        return temp