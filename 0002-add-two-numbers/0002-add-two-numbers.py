# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rem = 0
        d = dummy = ListNode()
        while rem or l1 or l2:
            curr = rem
            if l1:
                curr+=l1.val
                l1 = l1.next
            if l2:
                curr+=l2.val
                l2 =l2.next
            
            currNode = ListNode(val=curr%10)
            rem = curr//10
            dummy.next = currNode
            dummy = dummy.next
        
        return d.next
            
            