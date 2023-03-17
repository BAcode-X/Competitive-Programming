# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def search(self, root, depth):
        if root is None:
            return depth
        if root.left:
            left = self.search(root.left, depth + 1)
        if root.right:
            right = self.search(root.right, depth + 1)
        if root.left and root.right:
            return max(left, right)
        elif root.left:
            return left
        elif root.right:
            return right
        return depth

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            return self.search(root, 1)
        return 0
