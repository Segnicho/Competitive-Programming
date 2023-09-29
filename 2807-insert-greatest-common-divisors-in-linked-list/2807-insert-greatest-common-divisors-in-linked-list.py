# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def findGCD(a, b):
            while b:
                a, b = b, a % b
            return a

        dummy = head
        curr = head.next
        while curr:
            gcd = findGCD(curr.val, dummy.val)
            temp = curr
            tmp2 = curr.next
            b = ListNode(gcd)
            dummy.next = b
            b.next = curr
            dummy = temp
            curr = tmp2
        return head