def solution(food):
    answer = ''
    # food[i] : i번 음식의 수
    # food[0] : 물은 항상 1
    
    for i, amount in enumerate(food):
        answer += str(i) * (amount // 2)
    answer += ('0'+ answer[::-1])
    
    return answer # 대회를 위한 음식의 배치