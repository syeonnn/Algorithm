# from collections import deque

def solution(n, computers):
    
    answer = 0
    
#     def bfs(i):
#         queue = deque()
#         queue.append(i)
        
#         while queue:
#             i = queue.popleft()
#             visited[i]=1
            
#             for k in range(n):
#                 if computers[i][k]==1 and visited[k]==0:
#                     queue.append(k)
                    
                
#     visited = [0 for j in range(n)]
    
#     for i in range(n):
#         if not visited[i]:
#             bfs(i)
#             answer+=1

    def dfs(i):
        visited[i] = True
        for j in range(n):
            if not visited[j] and computers[i][j]==1:
                dfs(j)
        
    visited = [False]*(n)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer+=1
    
    return answer