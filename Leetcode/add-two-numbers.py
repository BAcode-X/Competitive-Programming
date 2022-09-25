"""
    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        f_num = ""
        it = l1
        while it.next != None:
            f_num += str(it.val)
            it = it.next
        f_num += str(it.val)
        s_num = ""
        it = l2
        while it.next != None:
            s_num += str(it.val)
            it = it.next
        s_num += str(it.val)
        f_num = int(f_num[::-1])
        s_num = int(s_num[::-1])
        ans = f_num + s_num
        ans = str(ans)[::-1]
        head = ListNode(val=ans[0])
        cp_head = head
        for i in ans[1:]:
            it = ListNode(val=i)
            head.next = it
            head = it
        return cp_head
