for i in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  a.sort()
  flag = 'YES'
  for j in range(1,n):
    if abs(a[j]-a[j-1]) > 1:
      flag = 'NO'
      break
  print(flag)
