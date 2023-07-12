class Solution:
    def __init__(self):
        self.root = []

    def find(self, x):
        if self.root[x] == x:
            return x
        return self.find(self.root[x])
    
    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a == b:
            return False
        self.root[a] = b
        return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        
        for i in range(n+1):
            self.root.append(i)
        for e in edges:
            val = self.union(e[0], e[1])
            if not val:
                return e
