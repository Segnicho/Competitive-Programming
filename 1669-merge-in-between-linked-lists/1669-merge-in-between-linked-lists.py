# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr1 = list1
        curr2 = list1
        
        i = 0
        secHead = None
        secTail = None
        while curr1:
            if i == a-1:
                secHead = curr1
            if i == b:
                secTail = curr1
                break
            curr1 = curr1.next
            i+=1 
        secHead.next= list2
        while curr2 and curr2.next:
            curr2 = curr2.next
        curr2.next = secTail.next
        return list1