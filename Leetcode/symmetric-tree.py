class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, left, right) -> bool:
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        else:
            return (left.val == right.val) and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
