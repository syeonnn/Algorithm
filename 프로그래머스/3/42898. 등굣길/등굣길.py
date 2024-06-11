def solution(m, n, puddles):
    # 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)] #n행 m열
    dp[1][1] = 1 
        
    for N in range(1, n+1):
        for M in range(1, m+1):
            if [M,N] in puddles:
                continue
            dp[N][M] += (dp[N][M-1] + dp[N-1][M]) % 1000000007
    
    return dp[n][m]