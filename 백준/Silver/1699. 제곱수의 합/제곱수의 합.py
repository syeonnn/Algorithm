import math

N = int(input())
answer = 0

# 그리디 방법, 반례 발견! 12 = 3^2+1+1+1 = 2^2+2^2+2^2

dp = [x for x in range(N+1)]

for i in range(2, N+1):
  for j in range(1, i+1):
    square = j**2

    if square > i:
      break

    if dp[i] > dp[i-square] + 1:
      dp[i] = dp[i-square] + 1

print(dp[N])