# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeList(l1, l2):
            dummy = tail = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            tail.next = l1 or l2
            return dummy.next
        
        n = len(lists)
        while n >= 2:
            k = math.ceil(n/2)
            for i in range(n//2):
                lists[i] = mergeList(lists[i], lists[i+k])
            n = k
        return lists[0] if lists else None
                