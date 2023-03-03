class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        cnt, n = 0, len(people)
        l, r = 0, n-1
        while l <= r:
            if people[l] + people[r] > limit:
                cnt += 1
                l += 1
            else:
                cnt += 1
                l += 1
                r -= 1
        return cnt
