def solution(triangle):
    answer = 0    
    row = len(triangle)
    dp = [[0 for _ in range(row+1)] for _ in range(row)]
    
    # dp, bottom-up으로 0번째 인덱스값부터 순서대로 탐색하며 최대합 저장
    for i in range(row):
        for idx, t in enumerate(triangle[i]): 
            if idx == 0:
                dp[i][idx] = t + dp[i-1][idx]
            elif idx == i:
                dp[i][idx] = t + dp[i-1][idx-1]
            else:
                dp[i][idx] = t + max(dp[i-1][idx-1], dp[i-1][idx])
    
    answer = max(dp[row-1])
    return answer