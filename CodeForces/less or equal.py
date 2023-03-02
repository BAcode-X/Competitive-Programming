n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
if k == n:
  ans = a[-1]
else:
  if k == 0:
    ans = a[k]-1
  elif a[k-1] == a[k]:
    ans = -1
  else:
    ans = a[k-1]
if ans == -1:
  print(-1)
elif ans == 0 or ans > 10**9:
  print(-1)
else:
  print(ans)
