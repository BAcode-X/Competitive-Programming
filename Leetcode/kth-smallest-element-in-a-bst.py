class Solution:
    def __init__(self):
        self.k = 0

    def find(self, root):
        if not root:
            return None
        left = self.find(root.left)
        if left:
            return left
        self.k -= 1
        if not self.k:
            return root.val
        return self.find(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        ans = self.find(root)
        return ans if ans else 0
