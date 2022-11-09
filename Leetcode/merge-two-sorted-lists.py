from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp = ListNode()
        head = tmp
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1, head = list1.next, list1
            else:
                head.next = list2
                list2, head = list2.next, list2
        if list1 or list2:
            head.next = list1 if list1 else list2
        
        return tmp.next
