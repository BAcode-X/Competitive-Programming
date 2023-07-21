class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_ = max(max(trip[2] for trip in trips), max(trip[1] for trip in trips))
        passengers = [0] * (max_ + 1)

        for trip in trips:
            passengers[trip[1]] += trip[0]
            passengers[trip[2]] -= trip[0]
        
        cur = 0
        for p_change in passengers:
            cur += p_change
            if cur > capacity:
                return False
        return True
