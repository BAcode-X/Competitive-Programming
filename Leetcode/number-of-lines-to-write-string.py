from string import ascii_lowercase

class Solution:
    def numberOfLines(self, width: List[int], s: str) -> List[int]:
        d = {i:j for i, j in zip(ascii_lowercase, width)}
        n = len(s)
        cnt = 0
        line_cnt = 0
        for i in range(n):
            if line_cnt + d[s[i]] <= 100:
                line_cnt += d[s[i]]
            else:
                line_cnt = d[s[i]]
                cnt += 1
        if line_cnt:
            cnt += 1
        return [cnt, line_cnt]
