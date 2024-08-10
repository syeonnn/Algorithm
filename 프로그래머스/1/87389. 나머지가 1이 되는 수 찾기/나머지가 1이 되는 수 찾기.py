def solution(n):
    answer = 0
    # n - 1 의 약수 중 1아닌 가장 작은 수
    for i in range(2, n):
        if (n-1) % i == 0:
            answer = i
            break
    return answer