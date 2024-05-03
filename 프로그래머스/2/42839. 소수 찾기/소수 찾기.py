import math
from itertools import permutations # combinations

def solution(numbers):
    answer = 0
    nums = list(numbers)
    
    cases = set()
    # 조합가능한 모든 경우 만들기 (순열)
    for i in range(1, len(nums)+1): # numbers 원소 중 i개를 조합
        permutationList = permutations(nums,i)
        for p in permutationList:
            pItem = int(''.join(p))
            cases.add(pItem)
            
     # 소수 찾기
    def isPrime(x):
        if x <= 1:
            return False
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False # 소수 X
        return True # 소수 O
    
    for x in cases:
        if isPrime(x):
            answer += 1
    
    return(answer)