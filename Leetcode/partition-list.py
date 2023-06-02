class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        less_head = less
        greater = ListNode()
        greater_head = greater
        
        tmp = head
        while tmp:
            if tmp.val < x:
                less.next = tmp
                less = less.next
            else:
                greater.next = tmp
                greater = greater.next
            tmp = tmp.next
        greater.next = None
        less.next = greater_head.next
        return less_head.next
        
