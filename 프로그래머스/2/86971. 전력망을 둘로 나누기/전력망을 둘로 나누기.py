from collections import deque

def solution(n, wires):
    answer = -1
    cnt = n
    
    def bfs(graph,x):   # 서로 연결되어있는 송전탐 개수 탐색-반환
        visited = [False for _ in range(n+1)]
        que = deque()
        que.append(x)
        visited[x] = True
        
        while que:
            curr = que.popleft()
            
            for next in graph[curr]:
                if not visited[next]:
                    visited[next] = True
                    que.append(next)                    
        
        return visited.count(True)
    
    for x,y in wires:   # 각각의 연결에 대해 차례대로 한 쌍씩 끊는다고 가정
        
        graph = [[] for _ in range(n+1)]
        # -번째 쌍 (x,y) 을 끊는 상황에서 graph 재구성
        for a,b in wires:
            if x == a and y == b:  # 끊으려는 해당 쌍이라면
                continue
            else:
                graph[a].append(b)
                graph[b].append(a)
        
        # 각각의 네트워크에서 연결되어 있는 송전탑 개수 카운트
        net_a = bfs(graph,x)
        net_b = bfs(graph,y)

        cnt = min(abs(net_a-net_b), cnt)
        
    return cnt # answer