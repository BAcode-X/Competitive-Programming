class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        
        left_ = self.hasPathSum(root.left, targetSum - root.val)
        right_ = self.hasPathSum(root.right, targetSum - root.val)
        
        return left_ or right_
