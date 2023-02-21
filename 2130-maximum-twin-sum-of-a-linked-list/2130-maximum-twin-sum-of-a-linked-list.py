# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        #partition
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        # reverse first part
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
            
        mx = 0
        while prev and second:
            mx = max(mx, prev.val+second.val)
            prev = prev.next
            second = second.next
        return mx
