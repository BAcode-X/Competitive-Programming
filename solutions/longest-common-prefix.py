"""
    Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_cnt = 99999999
        strs.sort(key=lambda x: len(x))
        if len(strs) > 1:
            for j in range(1, len(strs)):
                cnt = 0
                for i in range(len(strs[0])):
                    if strs[0][i] == strs[j][i]:
                        cnt += 1
                    else:
                        break
                min_cnt = min(min_cnt, cnt)
            return strs[0][:min_cnt]
        return strs[0]
