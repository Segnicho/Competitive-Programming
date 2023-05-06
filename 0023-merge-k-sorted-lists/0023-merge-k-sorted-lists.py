# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        for ls in lists:
            node = ls
            while node:
                res.append(node.val)
                node = node.next
        heapify(res)
        ans = []
        node = None
        if res:
            node = ListNode(heappop(res))
        dummy = node
        while res:
            node.next = ListNode(heappop(res))            
            node = node.next
        return dummy