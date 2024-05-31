import sys

input = sys.stdin.readline

n = int(input())
arr = [0 for _ in range(10001)]
for i in range(1, n+1):
  arr[i] = int(input())

# 포도주들의 관계
# dp[n] = (dp[n-1], arr[n]+arr[n-1]+dp[n-3], arr[n]+dp[n-2]) 중 가장 큰 값 갱신

dp = [0 for _ in range(10001)]
dp[1] = arr[1]
dp[2] = arr[1] + arr[2]

for i in range(3, n+1):
  dp[i] = max(dp[i-1], arr[i]+arr[i-1]+dp[i-3], arr[i]+dp[i-2])

print(max(dp))    