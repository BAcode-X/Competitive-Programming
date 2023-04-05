class Solution:
    def __init__(self):
        self.ans = []
    
    def traverse(self, cur, arr):
        arr.append(str(cur.val))
        if cur.left == None and cur.right == None:
            self.ans.append("->".join(arr))
            return
        if cur.left:
            self.traverse(cur.left, arr[:])
        if cur.right:
            self.traverse(cur.right, arr[:])
        

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.traverse(root, [])
        return self.ans
