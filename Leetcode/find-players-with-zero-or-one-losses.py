from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        val = defaultdict(lambda :[0,0])
        for match in matches:
            val[match[0]][0] += 1
            val[match[1]][1] += 1
        
        winners = []
        one_time = []
        for player in sorted(val):
            if val[player][1] == 0 and val[player][0] > 0:
                winners.append(player)
            if val[player][1] == 1:
                one_time.append(player)
        return [winners, one_time]
