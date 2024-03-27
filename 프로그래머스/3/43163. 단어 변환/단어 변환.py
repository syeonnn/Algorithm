# 최소! bfs! 덱큐
from collections import deque
def solution(begin, target, words):
    answer = 0
    visited = [False]*len(words)
    
    if target not in words:
        return answer
    
    def bfs(begin, target, words):
        # 비교대상 단어와 알파벳이 1개 차이나는 단어가 1개 이상일 수 있음
        # ( 해당 단어, 변환순서(횟수) ) 쌍으로 같이 저장해야 함!!
        
        que = deque()
        que.append((begin,0))
        
        while que:
            word,count = que.popleft()
            
            if target == word:   
                return count
            
            for i in range(len(words)):
                if not visited[i]:
                    temp_count = 0
                    for j in range(len(word)):
                        if word[j]!= words[i][j]:
                            temp_count+= 1

                    if temp_count == 1:
                        que.append((words[i],count+1))
                        visited[i] = True
        
    answer = bfs(begin, target, words)
    
    return answer
