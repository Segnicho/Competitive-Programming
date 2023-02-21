# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = head
        cnt = 1
        if not head or not head.next:
            return head
        while dummy.next:
            cnt+=1
            dummy = dummy.next
        k = k % cnt
        dummy.next = head
        for _ in range(cnt-k):
            head = head.next
            dummy = dummy.next
        dummy.next = None
        return head