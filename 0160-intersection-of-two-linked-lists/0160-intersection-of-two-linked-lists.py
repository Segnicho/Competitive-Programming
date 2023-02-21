# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        st = set()
        curr1 = headA
        curr2 = headB
        
        leng1 = 0
        leng2 = 0
        
        while curr1  or curr2:
            if curr1:
                leng1+=1
                curr1 = curr1.next
            if curr2:
                leng2+=1
                curr2 = curr2.next
        
        curr1 = headA
        curr2 = headB
        
        if leng1>leng2:
            for _ in range(leng1-leng2):
                curr1 = curr1.next
        elif leng2>leng1:
            for _ in range(leng2-leng1):
                curr2 = curr2.next
        while curr1:
            if curr1 == curr2:
                return curr1
            curr1 = curr1.next
            curr2= curr2.next
        return None