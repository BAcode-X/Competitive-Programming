from collections import defaultdict

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = defaultdict(int)
        for content in cpdomains:
            c, web = content.split()
            domains = web.split('.')
            for i in range(len(domains)):
                cnt['.'.join(domains[i:])] += int(c)
        ans = []
        for i in cnt:
            ans.append(f"{cnt[i]} {i}")
        return ans
