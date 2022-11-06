from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        i = head
        a = []
        while i.next is not None:
            a.append(i.val)
            i = i.next
        a.append(i.val)
        if a:
            ans = ListNode(val=a.pop(), next=None)
            h = ans
            while a:
                h.next = ListNode(val=a.pop())
                h = h.next
            return ans
        return ListNode(val=None, next=None)
