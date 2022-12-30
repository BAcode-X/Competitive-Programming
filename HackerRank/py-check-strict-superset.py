from collections import Counter
a = list(map(int, input().split()))
n = int(input())
d = Counter(a)
def ans(n):
    for i in range(n):
        b = list(map(int, input().split()))
        for j in b:
            if not d.get(j, None):
                return False
    return True
print(ans(n))
