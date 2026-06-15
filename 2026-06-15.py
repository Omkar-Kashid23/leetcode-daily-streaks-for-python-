# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:return None

        cnt = 0
        curr = head
        while curr != None:
            cnt += 1
            curr = curr.next

        mid = cnt//2

        curr = head
        current_step = 0
        
        while current_step < (mid-1):
            curr = curr.next
            current_step += 1

        curr.next = curr.next.next
        return head