# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode(next = head)
        curr = head
        
        while curr:
            dulpicate = False
            while curr.next and curr.val == curr.next.val:
                dulpicate = True
                curr = curr.next
            if dulpicate:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
        return dummy.next
        