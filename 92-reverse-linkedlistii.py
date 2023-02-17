# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head
        pos = 1
        curr = head
        pre = head
        while pos < left:
            if pos>1:
                pre = pre.next
            curr = curr.next
            pos+=1
        p = pos
        d = curr
        while p <= right:
            d = d.next
            p+=1
        prev = d
        hd = curr
        while pos <= right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            pos+=1
        if left != 1:
            hd.next = curr
            pre.next = prev
        else:
            return prev
        return head
