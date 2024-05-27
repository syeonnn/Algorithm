from collections import deque
import sys

input = sys.stdin.readline

T, W = map(int, input().split()) # T초 동안 자두 떨어짐, 자두는 W번만 움직임!
trees = [0] + [ int(input()) for _ in range(T)]
dp = [[0 for _ in range(W+1)] for _ in range(T+1)] # T초동안 W번 움직일 때 자두가 받을 수 있는 자두의 최대 개수

for t in range(1, T+1): # T초 동안
  # 위치 고정 == 이동횟수 0번인 경우
  if trees[t] == 1:
    dp[t][0] = dp[t-1][0]+1
  else:
    dp[t][0] = dp[t-1][0]

  # 이동횟수 W번인 경우
  for w in range(1, W+1): 
    # 자두 딸 수 있음 -> 자두 개수 +1
    if trees[t] == 1 and w % 2 == 0:
      dp[t][w] = max(dp[t-1][w], dp[t-1][w-1]) + 1
    elif trees[t] == 2 and w % 2 == 1:
      dp[t][w] = max(dp[t-1][w], dp[t-1][w-1]) + 1
    # 자두 못 땀
    else:
      dp[t][w] = max(dp[t-1][w], dp[t-1][w-1])


print(max(dp[-1])) # 자두가 받을 수 있는 자두의 최대 개수를 출력