from collections import Counter

def solution(participant, completion):   

    answer = Counter(participant) - Counter(completion)
    
    return list(answer.keys())[0] # 완주하지 못한 선수의 이름