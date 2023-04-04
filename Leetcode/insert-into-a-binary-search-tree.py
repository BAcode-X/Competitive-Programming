class Solution:

    def insert(self, node, val, prev):
        if node is None:
            if prev.val > val:
                prev.left = TreeNode(val=val)
            else:
                prev.right= TreeNode(val=val)
        else:
            if node.val > val:
                self.insert(node.left, val, node)
            else:
                self.insert(node.right, val, node)

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val=val)
        ans = root
        self.insert(root, val, root)
        return ans
