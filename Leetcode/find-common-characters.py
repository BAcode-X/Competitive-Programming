class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = list(words[0])
        for word in words[1:]:
            tmp = []
            for letter in word:
                if ans.__contains__(letter):
                    tmp.append(letter)
                    ans.remove(letter)
            ans = tmp
        return ans
