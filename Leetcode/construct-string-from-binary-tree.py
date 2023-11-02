class Solution:
    def __init__(self):
        self.ans = ''
    
    def preorder(self, root):
        if root is None:
            return
        self.ans += str(root.val)
        if root.left or root.right:
            self.ans += '('
            self.preorder(root.left)
            self.ans += ')'
            if root.right:
                self.ans += '('
                self.preorder(root.right)
                self.ans += ')'

    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.preorder(root)
        return self.ans
