class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = float('-inf')
        def dfs(root):
            if not root:
                return True
            left = dfs(root.left)
            if root.val <= self.prev:
                return False
            self.prev = root.val
            right = dfs(root.right)
            return left and right
        return dfs(root)
