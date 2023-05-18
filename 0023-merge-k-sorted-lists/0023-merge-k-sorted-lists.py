# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeTwoLists(n1, n2):
            tail = dummy = ListNode()
            while n1 and n2:
                if n1.val < n2.val:
                    tail.next = n1
                    n1 = n1.next
                else:
                    tail.next = n2
                    n2 = n2.next
                tail = tail.next
            tail.next = n1 or n2
            return dummy.next
        
        if not lists:
            return None
        n = len(lists)
        while n > 1:
            k = math.ceil(n/2)
            for i in range(n//2):
                lists[i] = mergeTwoLists(lists[i], lists[i+k])
            n = k
        return lists[0]
