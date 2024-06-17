N = int(input()) # 컴퓨터 수
lines = int(input()) # 네트워크에 연결되어 있는 컴퓨터 쌍의 수
computers = [list(map(int, input().split())) for _ in range(lines)]
visited = [False for _ in range(N+1)]
virus = 0

def dfs(x):
    global virus
    visited[x] = True
    
    for c1, c2 in computers:
        if c1 == x and not visited[c2]:
            virus += 1
            dfs(c2)
        elif c2 == x and not visited[c1]:
            virus += 1
            dfs(c1)
    return

dfs(1)

print(virus)