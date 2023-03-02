# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        ans = cur
        if cur is None:
            return ans
        prev = cur.val
        while cur.next is not None:
            tmp = cur.next
            if tmp.val == prev:
                cur.next = tmp.next
            else:
                cur = cur.next
                if cur is not None:
                    prev = cur.val
        return ans
