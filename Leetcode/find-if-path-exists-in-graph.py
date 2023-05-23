from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        queue = deque([source])

        while queue:
            curr = queue.popleft()
            if curr == destination:
                return True

            for neighbour in graph[curr]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        
        return False
