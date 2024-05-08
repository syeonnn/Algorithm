import sys
from bisect import bisect_left, bisect_right
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [A[0]]

for i in range(N): 
  # 맨 마지막 원소보다 현재 위치의 원소가 더 크다면
  if dp[-1] < A[i]:
    dp.append(A[i])
  else:
    idx = bisect_left(dp,A[i])
    dp[idx] = A[i]

print(len(dp))  # 가장 긴 증가하는 부분 수열의 길이