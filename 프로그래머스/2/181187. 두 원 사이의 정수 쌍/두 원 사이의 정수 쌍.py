import math

def solution(r1, r2):
    answer = 0
    
    # 작은 원 위의 4개 점 + 큰 원 위의 4개 점 + 그 사이 공간의 점 개수 * 4
    
    # 큰 원에서 y좌표값 - 작은 원에서 y좌표값
    # x**2 + y**2 = r**2 -> Math.sqrt(r**2 - x**2)
    for i in range(1, r2+1):
        e = math.floor(math.sqrt(r2**2 - i**2)) # 큰 원 내부
        if r1 > i:
            s = math.ceil(math.sqrt(r1**2 - i**2)) # 작은 원 외부
        else:
            s = 0
        answer += e - s + 1
    
    answer = answer*4 
    
    return answer