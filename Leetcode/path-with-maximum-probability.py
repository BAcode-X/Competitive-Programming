from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        max_probabilities = [0.0] * n
        max_probabilities[start_node] = 1.0
        priority_queue = [(-1.0, start_node)]

        while priority_queue:
            prob, node = heapq.heappop(priority_queue)
            prob = -prob

            if node == end_node:
                return prob

            if prob < max_probabilities[node]:
                continue

            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > max_probabilities[neighbor]:
                    max_probabilities[neighbor] = new_prob
                    heapq.heappush(priority_queue, (-new_prob, neighbor))

        return 0.0
