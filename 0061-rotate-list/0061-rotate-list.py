# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        last_val = head
        length = 1

        while last_val.next:
            last_val = last_val.next
            length += 1

        k = k % length

        last_val.next = head

        temp = head

        for _ in range(length - k - 1):
            temp = temp.next

        res = temp.next
        temp.next = None

        return res