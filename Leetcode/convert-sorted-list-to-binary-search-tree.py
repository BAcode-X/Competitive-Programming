class Solution:
    def getMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = None
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if prev:
            prev.next = None
        return slow

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return head
        if not head.next:
            return TreeNode(val=head.val)
        mid = self.getMiddle(head)
        root = TreeNode(val=mid.val)
        root.right = self.sortedListToBST(mid.next)
        mid.next = None
        root.left = self.sortedListToBST(head)
        return root
