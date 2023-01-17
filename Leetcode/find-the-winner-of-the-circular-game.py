class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i+1 for i in range(n)]
        ind = 0
        while len(friends) > 1:
            friends.pop((ind + k - 1) % n)
            ind = (ind + k - 1) % n
            n -= 1
        return friends[0]
