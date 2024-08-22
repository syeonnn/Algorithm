from collections import Counter

def solution(participant, completion):   
    temp = {}
    temp_sum = 0
    
    # 해시함수 활용
    for part in participant:
        temp[hash(part)] = part
        temp_sum += hash(part)
    for comp in completion:
        temp_sum -= hash(comp)
        
    answer = temp[temp_sum]
    
    return answer # 완주하지 못한 선수의 이름