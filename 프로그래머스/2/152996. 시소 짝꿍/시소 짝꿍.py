from collections import Counter

def solution(weights):
    answer = 0
  
    counter = Counter(weights)
    # 같은 무게의 사람이 2명이상인 경우
    for k,v in counter.items():
        if v > 1:
            answer += v * (v-1) // 2

    weights = set(weights)
    print(type(weights))
    # weights의 길이가 길기 때문에 이중 for 문 이용시 시간 초과
    # 배열 요소로 1회씩만 탐색하도록 함
    for w in weights:
        if w * 1/2 in weights:
            answer += counter[w] * counter[w * 1/2]
        if w * 3/4 in weights:
            answer += counter[w] * counter[w * 3/4]
        if w * 3/2 in weights:
            answer += counter[w] * counter[w * 3/2]
        

    return answer