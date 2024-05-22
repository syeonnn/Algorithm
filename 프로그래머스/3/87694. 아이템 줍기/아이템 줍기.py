from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    min_x, min_y = 51, 51
    max_x, max_y = 0, 0
    # rectangle 만큼의 모든 좌표 값들을 1로 저장
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    visited = [[0 for _ in range(102)] for _ in range(102)]
    
    # 하나의 graph로 통합
    for locs in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2,locs)
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2: # 테두리 제외 내부만 표시
                    graph[i][j] = 0
                elif graph[i][j] != 0:  # 한 사각형의 테두리가 다른 사각형의 내부에 포함되면 길로 인정x
                    graph[i][j] = 1
    
    # 테두리 연속되는 경우, 잘못된 경로 설정 방지하기 위해 각 2배!
    cx, cy, ix, iy = 2*characterX, 2*characterY, 2*itemX, 2*itemY

    def bfs(x, y):
        que = deque()
        que.append((x,y))
        
        while que:
            x, y = que.popleft()
            
            if x == ix and y == iy:
                return visited[x][y] // 2
            
            for dx, dy in ([-1,0],[1,0],[0,-1],[0,1]):
                nx = x + dx
                ny = y + dy
                
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    que.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
    
    answer = bfs(cx, cy)

    return answer