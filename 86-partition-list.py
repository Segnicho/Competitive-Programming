# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        ls = []
        grt = []
        while head:
            if head.val < x:
                ls.append(head.val)
            else:
                grt.append(head.val)
            head = head.next
        headNode = ListNode(None)
        dummy = headNode
        for el in ls:
            newNode = ListNode(el)
            headNode.next = newNode
            headNode = headNode.next
        for el in grt:
            newNode = ListNode(el)
            headNode.next = newNode
            headNode = headNode.next
        return dummy.next

    
