for t in range(int(input())):
  n,m = map(int, input().split()) # n행 m열
  array = list(map(int, input().split()))
  dp = []
  for idx in range(n):
    dp.append(array[idx*m:idx*m+m])
  print(dp)
  # array[i][j] = i행 j열에 존재하는 금의 양
  # dp[i][j] = i행 j열까지의 최적해 (얻을 수 있는 금의 최댓값)
  # 점화식 : dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

  # m개의 열 각각에 대해 왼쪽에 위치한 값들 비교합산 (바텀업)
  for j in range(1, m):
    for i in range(n):
      left_up = 0 if i == 0 else dp[i-1][j-1]
      left = dp[i][j-1]
      left_down = 0 if i == n-1 else dp[i+1][j-1]
      
      dp[i][j] = dp[i][j] + max(left_up, left, left_down)

  result = 0
  for k in range(n):   # n개 행 각각의 첫번째 열에서 시작하는 경우들 가운데 최댓값 구하기
    result = max(result, dp[k][m-1])
  print(result)
    
    
