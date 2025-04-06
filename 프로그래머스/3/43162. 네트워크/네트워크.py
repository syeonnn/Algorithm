def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    def dfs(x):
        visited[x] = True
        
        for j in range(n):
            if not visited[j] and computers[x][j] == 1:
                dfs(j)
            
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
        
    return answer