from collections import deque

def solution(arr):
    answer = [arr[0]] + []
    
    cmp = arr[0]
    
    for a in arr[1:]:
        if cmp == a:
            continue
        else:
            answer.append(a)
            cmp = a
            
    return answer