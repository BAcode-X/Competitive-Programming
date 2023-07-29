import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = Counter(words)
        min_heap = [(-freq, word) for word, freq in word_freq.items()]
        heapq.heapify(min_heap)

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(min_heap)[1])
        
        return ans
