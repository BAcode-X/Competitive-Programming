class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        words = []
        prev = 0
        for i in spaces:
            words.append(s[prev:i])
            prev = i
        words.append(s[prev:])
        return ' '.join(words)
