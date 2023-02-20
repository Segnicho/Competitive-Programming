# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        stck = []
        idx = 0
        while head:
            ans.append(0)
            while stck and head.val > stck[-1][1]:
                lstVal = stck.pop()
                ans[lstVal[0]] = head.val
            stck.append([idx, head.val])
            idx+=1
            head = head.next
        return ans
        