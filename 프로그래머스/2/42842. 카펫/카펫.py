import math

def solution(brown, yellow):
    answer = []
    
    for i in range(1, int(math.sqrt(yellow))+1):
        if yellow % i == 0:
            yh = i
            yw = yellow // i
            if brown == (yh+yw)*2 + 4:
                answer = [yw+2, yh+2]
    return answer