def solution(targets):
    answer = 0

    # 끝점 기준 오름차순 정렬
    targets.sort(key = lambda x: (x[1], x[0]))

    # 그리디 알고리즘
    cmp = 0
    for target in targets:
        if target[0] >= cmp:    # 시작점이 (이전 끝점)비교지점 보다 크다면 == 겹치지 않는다면
            answer += 1
            cmp = target[1]
    
    # 모든 폭격 미사일을 요격하기 위해 필요한 요격 미사일 수의 최솟값
    return answer