n = int(input())
array = []
for _ in range(n):
  array.append(list(map(int, input().split())))

array.sort(key = lambda x: x[0]) # A 전봇대에 연결된 번호 기준 정렬
dp = [1 for _ in range(n)]

for i in range(1,n):
  for j in range(0,i):
    if array[j][1] < array[i][1]:
      # 교차하지 않는다면
      dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))