from itertools import product

def solution(word):
    answer = 0
    alpha = ['A','E','I','O','U']
    result = []
    
    for i in range(1,6):
        for p in product(alpha, repeat = i):
            result.append(''.join(p))
    
    result.sort()
    answer = result.index(word) + 1
    return answer