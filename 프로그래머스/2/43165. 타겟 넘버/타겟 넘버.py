from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append((numbers[0],0))
    queue.append((-1*numbers[0],0))
    
    # BFS
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx == n:
            if temp == target:
                 answer+=1
        else:
            queue.append((temp+numbers[idx],idx)) 
            queue.append((temp-numbers[idx],idx)) 
                   
    return answer

    #DFS
    def dfs(idx,result):
        if idx == n:
            # target 값이면
            if result == target:
                nonlocal answer
                answer+=1
            # 아니면
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])

    # numbers 배열의 첫 번째 원소부터 탐색
    # dfs(0, 0)
    
