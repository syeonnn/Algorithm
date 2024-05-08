import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(N): 
  for j in range(i):
    if A[i] > A[j]:
      dp[i] = max(dp[i], dp[j] + 1)
      # 수열 A의 i번째 원소에 대해 0~i-1번째 원소들 전체 중에 가장 긴 증가하는 수열을 만들기 위해
      # 앞에서부터 dp값 구하며 max 비교가 필요함

print(max(dp))