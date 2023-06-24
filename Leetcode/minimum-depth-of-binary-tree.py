class Solution:

    def dfs(self, root, cnt):
        if root == None:
            return cnt
        if root.left == None and root.right == None:
            return cnt + 1
        if root.left == None:
            return self.dfs(root.right, cnt + 1)
        if root.right == None:
            return self.dfs(root.left, cnt + 1)
        return min(self.dfs(root.left, cnt + 1), self.dfs(root.right, cnt + 1))

    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
