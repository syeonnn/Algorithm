from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    answer = 0
    # 0은 빈 땅, 1은 석유
    # bfs/dfs로 탐색하면서 해당 좌표에서 인접한 석유량으로 land 좌표값 업데이트
    visited = [[False] * (m) for _ in range(n)]
    result = [0 for _ in range(m+1)]
     
    def bfs(x,y): # 행, 열
        que = deque()
        que.append((x,y))
        visited[x][y] = True
        min_y, max_y = y, y
        size = 1
             
        while que:
            x,y = que.popleft()
            min_y, max_y = min(min_y, y), max(max_y, y)
        
            for dx,dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx,ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and land[nx][ny] == 1:
                    que.append((nx,ny))
                    visited[nx][ny] = True
                    size += 1
                    
        # 열 별로 계산된 석유 값 더하기
        for col in range(min_y, max_y + 1): # for _ in _ VS for _ in range_ 차이 주의하기!!
            result[col] += size
    
    for N in range(n): # 세로길이 = 행
        for M in range(m): # 가로길이 = 열
            if land[N][M] == 1 and not visited[N][M]:
                bfs(N,M)
    
    # 시추관 하나를 설치해 뽑을 수 있는 가장 많은 석유량
    answer = max(result)

    return answer