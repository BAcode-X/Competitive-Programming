class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        ind = 1
        cur = head
        stack = []
        tmp_head = ListNode()
        tmp = tmp_head
        while cur.next != None:
            if ind == right:
                stack.append(cur.val)
                while stack:
                    tmp.next = ListNode(val=stack.pop())
                    tmp = tmp.next
            elif ind >= left and ind < right:
                stack.append(cur.val)
            else:
                tmp.next = ListNode(val=cur.val)
                tmp = tmp.next
            cur = cur.next
            ind += 1
        if ind == right:
            stack.append(cur.val)
            cur = cur.next
        while stack:
            tmp.next = ListNode(val=stack.pop())
            tmp = tmp.next
        if cur:
            tmp.next = ListNode(val=cur.val)
        return tmp_head.next
