# arr = [0~9 구성 배열... 연속없게 전부 제거]
from collections import deque

def solution(arr):    
    arr = deque(arr)
    x = arr.popleft()
    answer = deque([x])
    
    for a in range(len(arr)):
        y = arr.popleft()
        
        if x == y:
            continue
        else:
            answer.append(y)
            x = y
            
    return list(answer)
    