from collections import deque

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    # dfs, bfs로 모든 경우를 탐색
    
    def bfs(num,idx):    
        cnt = 0
        que = deque()
        que.append((num,idx))
        que.append((-num,idx))

        while que:
            num, idx = que.popleft()
            idx += 1
            
            if idx == n: # 단문으로 2가지 조건 합칠 수 없음! 아래 조건문 else와의 관계에 유의!
                if num == target:
                    cnt += 1
            else:
                # for calc in [-1,1]:
                que.append((num + numbers[idx],idx))
                que.append((num - numbers[idx],idx))
                
        return cnt
        
    answer = bfs(numbers[0],0)
    return answer
