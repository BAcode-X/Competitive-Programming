class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        arr = []
        if cur != None:
            while cur.next:
                arr.append(cur.val)
                cur = cur.next
            arr.append(cur.val)
            arr.sort()
        cur = head
        for i in arr:
            cur.val = i
            cur = cur.next
        return head
