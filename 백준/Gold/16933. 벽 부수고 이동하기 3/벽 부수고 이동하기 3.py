from collections import deque
n, m, k = map(int, input().split())
grid = [list(str(input())) for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
# 1: 낮, -1: 밤

def bfs():
    q = deque()
    q.append((0, 0, 1, 0))
    visited = [[[0 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1
    time = 1
    while q:
        for _ in range(len(q)):
            y, x, dist, cnt = q.popleft()
            if (y, x) == (n-1, m-1):
                return dist
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx][cnt]:
                    if grid[ny][nx] == '0':
                        visited[ny][nx][cnt] = dist+1
                        q.append((ny, nx, dist+1, cnt))
                    elif grid[ny][nx] == '1':
                        if cnt+1 <= k and not visited[ny][nx][cnt+1]:
                            if time == 1:
                                visited[ny][nx][cnt+1] = dist+1
                                q.append((ny, nx, dist+1, cnt+1))
                            else:
                                q.append((y, x, dist+1, cnt))
        time *= (-1)
    return -1
print(bfs())