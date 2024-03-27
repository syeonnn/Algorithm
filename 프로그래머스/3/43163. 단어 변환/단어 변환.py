# 최소! bfs! 덱큐
from collections import deque
def solution(begin, target, words):
    answer = 0
    visited = [False]*len(words)
    
    if target not in words:
        return answer
    
    def bfs(begin, target, words):
        count = 0
        
        que = deque()
        que.append((begin,0))
        
        while que:
            word,count = que.popleft()
            
            if target == word:   
                return count
            
            for i in range(len(words)):
            # print(f'{i}번째 words 배열요소: {words[i]}')
                if not visited[i]:
                    temp_count = 0
                    for j in range(len(word)):
                        if word[j]!= words[i][j]:
                            temp_count+= 1
                            # print(f'{word}와 비교했을때 {temp_count}만큼 차이발생')
                    if temp_count == 1:
                        que.append((words[i],count+1))
                        visited[i] = True
                        # print(f"1만큼 차이남=>{count}증가")
                        # print(f"que에 {words[i]}추가")
        
    # 비교대상 단어와 알파벳이 1개 차이나는 단어가 1개 이상일 수 있음
    # 해당 단어들을 변환순서(횟수)을 나타나는 값과 쌍으로 같이 저장해야 함!!
    answer = bfs(begin, target, words)
    
    return answer