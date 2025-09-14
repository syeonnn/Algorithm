from collections import deque

def solution(arr):
    
    arr = deque(arr)
    ans = [arr.popleft()]
    
    for i in range(len(arr)):
        a = arr.popleft()
        if a != ans[-1]:
            ans.append(a)   
    
    return ans