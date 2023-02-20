# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev =curr = head 
        if head == None:
            return head
        while curr:
            if(prev.val != curr.val):
                prev.next = curr
                prev = prev.next
            curr = curr.next
        prev.next = None
        return head
