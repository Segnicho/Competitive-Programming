# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def middle(head):
            slow, fast = head, head
            while fast and fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def merge(h1, h2):
            dummy = ListNode(None)
            node = dummy
            while h1 and h2:
                if h1.val < h2.val:
                    node.next = h1
                    h1 = h1.next
                else:
                    node.next = h2
                    h2 = h2.next
                node = node.next
            node.next = h1 or h2
            return dummy.next

        
        if head is None or head.next is None:
            return head
        middle = middle(head)
        right_head = middle.next
        middle.next = None
        return merge(self.sortList(head),self.sortList(right_head))        
