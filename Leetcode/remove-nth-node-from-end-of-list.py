from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head:
            a = []
            while head.next is not None:
                a.append(head.val)
                head = head.next
            a.append(head.val)
            a.pop(-n)
            if a:
                ans = ListNode(val=a.pop(0))
                h = ans
                while a:
                    h.next = ListNode(val=a.pop(0))
                    h = h.next
                return ans
        return None