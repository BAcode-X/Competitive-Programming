class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tmp = ListNode(0)
        tmp.next = head

        i, cur = tmp, head
        while cur:
            if cur.next and cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                i.next = cur.next
            else:
                i = cur
            cur = cur.next
        return tmp.next
