import sys
input = sys.stdin.readline

sen1 = list(input())
sen2 = list(input())

dp = [[0 for _ in range(len(sen2))] for _ in range(len(sen1))]

for i in range(1,len(sen1)):
  for j in range(1,len(sen2)):
    if sen1[i-1] == sen2[j-1]:
      dp[i][j] = dp[i-1][j-1] + 1
    else:
      dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])