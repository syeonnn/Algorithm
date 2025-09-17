from collections import deque

def solution(priorities, location):
    
    # location 위치의 프로세스가 몇 번쨰로 실행되는지
    answer = 0
    
    priorities = deque(enumerate(priorities))
    
    while priorities:
        n, p = priorities.popleft() # 1.
        
        if any(p < comp for _, comp in priorities):
            priorities.append((n, p)) # 2.
        else:
            answer += 1
            if n == location:
                return answer
