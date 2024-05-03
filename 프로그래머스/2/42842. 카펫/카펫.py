import math

def solution(brown, yellow):
    answer = []
    
    # 중앙 노란색, 테두리 1줄 갈색
    for i in range(1, int(math.sqrt(yellow))+1):
        if yellow % i == 0:
            yw = yellow // i
            yh = i
            if (yw*2 + yh*2 + 4) == brown:
                answer.append(yw +2)
                answer.append(yh +2)
                return answer
                