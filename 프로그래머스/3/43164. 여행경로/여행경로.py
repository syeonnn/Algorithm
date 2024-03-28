from collections import deque

def solution(tickets):
    answer = []
    que = deque()
    que.append(('ICN',['ICN'],[]))

    while que:
        e, path, visited = que.popleft()

        if len(visited) == len(tickets):
            answer.append(path)
            #print(answer)
            
        for idx, ticket in enumerate(tickets):
            if not idx in visited and e == ticket[0]:
                que.append((ticket[1], path+[ticket[1]], visited+[idx]))
                        
    answer.sort()
    return answer[0]