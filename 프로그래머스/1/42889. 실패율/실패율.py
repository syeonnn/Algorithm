from collections import defaultdict

def solution(N, stages):
    answer = []
    result = defaultdict(int)
    temp = defaultdict(int)
    
    for s in stages:
        result[s] += 1
    
    for i in range(1,N+1):
        if result[i] == 0:
            temp[i] = 0
        else:
            temp[i] = result[i] / sum(result.values())
        del result[i]
    
    answer = sorted(temp.items(), key = lambda x: (-x[1],x[0]))
    answer = [ a[0] for a in answer ]
    
    return answer