# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        leng = 0
        arr = []
        print(head)
        while curr:
            arr.append(curr)
            curr = curr.next
            leng += 1
        print(leng)
        i = 0
        cur = head
        if leng == n:
            if not head or not head.next:
                return None
            else:
                head = head.next
                return head
        print(arr)
        arr[leng - n - 1].next = arr[leng - n + 1] if leng - n + 1 < leng else None
        return head
    
    
