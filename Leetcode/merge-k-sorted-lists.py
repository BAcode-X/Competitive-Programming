class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for i in lists:
            tmp = i
            while tmp:
                arr.append(tmp.val)
                tmp = tmp.next
        arr.sort()
        ans = ListNode()
        head = ans
        for i in arr:
            tmp = ListNode(i)
            ans.next = tmp
            ans = ans.next
        
        return head.next
