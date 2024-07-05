def solution(m, n, puddles):
    
    dp = [[0] * (m+1) for _ in range(n+1)]
    # 각각의 좌표에서 대해 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수
    dp[1][1] = 1
    
    for N in range(1, n+1):
        for M in range(1, m+1):
            if [M,N] in puddles:
                continue
            
            # 물 웅덩이로 인해 초기화되지 않았을 수 있음
            # 따라서, dp[N][M] = dp[N-1][M] + dp[N][M-1]는 틀린 코드
            dp[N][M] += dp[N-1][M] + dp[N][M-1]
                     
    return dp[n][m] % 1000000007
