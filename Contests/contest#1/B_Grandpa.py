from collections import Counter
a = Counter(input().split())
print("YES" if len(a) > 4 else "NO")
