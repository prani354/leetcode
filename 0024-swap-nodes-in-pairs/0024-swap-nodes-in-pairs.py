# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        curr = head
        dummy = ListNode(0,head)

        prev = dummy
        while curr and curr.next:
            st = curr.next.next
            nxt = curr.next
            nxt.next = curr
            curr.next = st
            prev.next = nxt
            
            prev = curr
            curr = st

        return dummy.next
