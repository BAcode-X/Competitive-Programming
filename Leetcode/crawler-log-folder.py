class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for i in logs:
            if i == '../':
                if cnt:
                    cnt -= 1
            elif i == './':
                pass
            else:
                cnt += 1
        return cnt
