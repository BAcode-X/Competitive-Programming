class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (len(x), x))
        longest = ""
        built_words = set([""])
        
        for word in words:
            if word[:-1] in built_words:
                built_words.add(word)
                if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                    longest = word
                    
        return longest
