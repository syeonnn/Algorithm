from itertools import permutations
import math

def solution(numbers):
    answer = 0
    
    # 순열조합
    convert_numers = list(numbers)
    nums = set()
    
    for j in range(1, len(numbers)+1):
        perm_numbers = permutations(convert_numers, j)
        for p in perm_numbers:
            num = int(''.join(p))
            nums.add(num)
    
    def prime(num):
        # 초기화: 0과 1은 소수가 아니며, 2를 제외한 짝수는 미리 제거
        if num <= 1:
            return False;
        if num != 2 and num % 2 == 0:
            return False
        
        # 3부터 sqrt(n)까지 홀수만 검사
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
            
        return True;
    
    for n in nums:
        if prime(n):
            answer += 1
            
    return answer;