import sys
input = sys.stdin.readline

N = int(input())
array = [list(map(int, input().split())) for _ in range(N)]

dp = [0 for _ in range(N+1)]

# 재귀
# def dfs(n,sum):
#   global ans
#   # 종료 조건
#   if n == N:
#     ans = max(ans, sum)
#     return

#   if n+array[n][0] <= N: # 상담 가능하다면
#     dfs(n+array[n][0], sum+array[n][1])
#   dfs(n+1, sum) # 항상 (상담하지 않는다면)

# ans = 0
# dfs(0,0)
# print(ans)

# bottom-up
for i in range(N):
  for j in range(i+array[i][0], N+1): # dp[j] = i번째 상담까지 진행한 경우 j번째 상담 때 최대 누적 이익
    if dp[j] < dp[i] + array[i][1]:
      dp[j] = dp[i] + array[i][1] # 최대 누적 이익 갱신
print(dp[-1])

# top-down
#
