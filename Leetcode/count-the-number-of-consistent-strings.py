from collections import Counter

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_dict = Counter(allowed)
        cnt = 0
        for word in words:
            flag = True
            for letter in word:
                if not allowed_dict.get(letter, None):
                    flag = False
                    break
            if flag:
                cnt += 1
        return cnt
