from itertools import accumulate

n, m = map(int, input().split())

pref = [0]*(n+1)

for i in range(m):
  a = list(map(int, input().split()))
  pref[a[0]-1] += a[2]
  pref[a[1]] -= a[2]

print(max(accumulate(pref)))
