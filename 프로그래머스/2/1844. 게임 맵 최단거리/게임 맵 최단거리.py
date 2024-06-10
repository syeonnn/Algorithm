from collections import deque

def solution(maps):
    
    def bfs():
        n = len(maps)
        m = len(maps[0])
        
        que = deque()
        que.append((0,0))
        
        while que:
            x,y = que.popleft()
            if x==n-1 and y==m-1:
                return maps[x][y]
            
            for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                nx,ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m and maps[nx][ny]==1:
                    maps[nx][ny] = maps[x][y] + 1
                    que.append((nx,ny))
        return -1
                    
    answer = bfs()
    return answer