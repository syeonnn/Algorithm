def solution(sizes):
    answer = 0
    # 긴 변은 최대한 길게, 짧은 변은 짧은 길이 중에 가장 길게
    w = max(max(x) for x in sizes)
    h = max(min(y) for y in sizes)
    answer = w * h
    return answer