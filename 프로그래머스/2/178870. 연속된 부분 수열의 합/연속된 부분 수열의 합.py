def solution(sequence, k):
    answer = []
    end = 0
    interval_sum = 0
    
    for start in range(len(sequence)):
        while interval_sum < k and end < len(sequence):
            interval_sum += sequence[end]
            end += 1
        if interval_sum == k:
            answer.append([start, end-1])
        interval_sum -= sequence[start]
    
    # 길이가 짧은 수열, 그 중에서 시작 인덱스가 작은 수열 우선순위로 정렬
    answer.sort(key = lambda x : (x[1]-x[0], x[0]))
    
    return answer[0] # 부분 수열의 시작 인덱스와 마지막 인덱스를 담은 배열