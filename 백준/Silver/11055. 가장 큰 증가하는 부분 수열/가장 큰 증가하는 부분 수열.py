N = int(input())
A = list(map(int, input().split()))
d = [0 for _ in range(N)]

d[0] = A[0]

for i in range(N):
  for j in range(i):
    if A[i] > A[j]:
      d[i] = max(d[j] + A[i],d[i])
    else:
      d[i] = max(d[i],A[i])

print(max(d))