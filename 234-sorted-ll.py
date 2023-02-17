# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
#         split to two lists
        while fast and fast.next:
            slow,fast = slow.next, fast.next.next
        prev = None
#         reverse the right
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        lptr = head
        rptr= prev
        while rptr:
            if lptr.val != rptr.val:
                return False
            lptr = lptr.next
            rptr = rptr.next            
        return True
