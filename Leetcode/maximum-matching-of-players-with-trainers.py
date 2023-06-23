class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        n = len(players)
        m = len(trainers)
        trainers.sort()
        players.sort()
        cnt = 0
        left, right = 0, 0
        while left < n and right < m:
            if players[left] <= trainers[right]:
                cnt += 1
                left += 1
            right += 1
        return cnt
