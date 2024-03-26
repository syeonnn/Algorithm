# 일단, 최단거리!! BFS, 큐
# maps = list(map(int, input().split()))
from collections import deque
def solution(maps):
    answer = 0
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs(x,y):
        queue = deque()
        queue.append((x,y))

        while queue:
            x,y = queue.popleft()
    
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # map 범위 안, 방문x, 벽x
                if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny]==1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx,ny))
        return maps[len(maps)-1][len(maps[0])-1]

    answer = bfs(0,0)
    return -1 if answer == 1 else answer