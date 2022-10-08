from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = head
        cnt = 1
        ind = head
        while ind.next is not None:
            cnt += 1
            if cnt % 2 == 0:
                mid = mid.next
            ind = ind.next
        return mid
