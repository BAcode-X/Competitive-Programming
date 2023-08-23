from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seqs = defaultdict(int)
        ans = []

        for i in range(len(s) - 9):
            sq = s[i:i+10]
            seqs[sq] += 1

            if seqs[sq] == 2:
                ans.append(sq)

        return ans
