# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = head
        slow = head

        for i in range(k - 1):
            fast = fast.next
        f = fast
        while fast.next:
            fast = fast.next
            slow = slow.next
        f.val, slow.val = slow.val, f.val
        return head
    