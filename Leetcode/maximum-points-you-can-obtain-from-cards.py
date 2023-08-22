class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        def check(i, j, k, pref):
            x = pref[i+k] - pref[i]
            y = pref[j+1] - pref[j+1-k]
            return x, y
        
        pref = [0] + list(accumulate(cardPoints))
        n = len(cardPoints)
        left, right = 0, n - 1
        ans = 0
        while k:
            x, y = check(left, right, k, pref)
            if x > y:
                ans += cardPoints[left]
                left += 1
            else:
                ans += cardPoints[right]
                right -= 1
            k -= 1
        return ans
