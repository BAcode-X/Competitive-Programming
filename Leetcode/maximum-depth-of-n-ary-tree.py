class Solution:
    
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        dep = 0
        for node in root.children:
            dep = max(dep, self.maxDepth(node))
        
        dep += 1
        return dep
