import math

def solution(number, limit, power):
    answer = 0
    divisor = []
    
    # 약수 개수 구하는 로직 간소화 : 제곱근까지 연산 math.sqrt(2) / **(1/2)
    # 약수 == 제곱수이면 cnt += 1
    # 아니면 cnt += 2
    
    for num in range(1, number+1):
        divisor_cnt = 0
        for n in range(1, int(math.sqrt(num)) + 1):
            if num % n == 0:
                if n == math.sqrt(num):
                    divisor_cnt += 1
                else:
                    divisor_cnt += 2
        
        if divisor_cnt > limit:
            divisor_cnt = power
            
        divisor.append(divisor_cnt)
        
    answer = sum(divisor)
    
    return answer