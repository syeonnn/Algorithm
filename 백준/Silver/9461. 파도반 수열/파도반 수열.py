from collections import defaultdict
import sys
input = sys.stdin.readline

# dp = [0,1,1,1] + [0 for _ in range(97)]
dp = defaultdict(int)
dp[1] = 1
dp[2] = 1
dp[3] = 1
  
T = int(input()) # 테케
for _ in range(T):
  N = int(input())
  
  if dp[N]:
    print(dp[N])
    
  else:
    for i in range(4, N+1):
      dp[i] = dp[i-2] + dp[i-3]
    print(dp[N])
