# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr = head
        dummy.next = head
        count = 0
        

        while curr:
            count += 1
            curr = curr.next

        curr = head.next
        temp = dummy
        for _ in range(count-n):
            temp = temp.next
            curr = curr.next

        temp.next = curr

        return dummy.next



            
