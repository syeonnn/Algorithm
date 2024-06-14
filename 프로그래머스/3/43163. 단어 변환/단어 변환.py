from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [False]*len(words)
    
    if target not in words:
        return answer
    
    # begin -> target
    # words배열에서 begin과 알파벳 한 개 차이나는 단어들이 1개 이상일 수 있음
    # 따라서 각 단어까지의 변환횟수를 que에 같이 저장한다.
    # 통합해서 횟수 계산X 단어별, 케이스별 연산O
        
    def bfs():
        que = deque()
        que.append((begin,0))
        
        while que:
            word,cnt = que.popleft()
            
            if word == target:
                return cnt
            
            for i in range(len(words)):
                if not visited[i]:
                    tcnt = 0
                    for j in range(len(word)):
                        if word[j] != words[i][j]:
                            tcnt += 1
                        else:
                            continue
                    if tcnt == 1: # 한 개의 알파벳만 다를 때
                        que.append((words[i],cnt+1))
                        visited[i] = True
                    
        return 0
    
    answer = bfs()
    return answer       