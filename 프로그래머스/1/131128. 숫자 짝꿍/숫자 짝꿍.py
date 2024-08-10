def solution(X, Y):
    answer = ''
    # X, Y 각각에 대해 dict 타입으로 정보 뽑기
    x_dict = dict()
    y_dict = dict()
    result = ''
    
    for x in X:
        if x in x_dict:
            x_dict[x] += 1
        else:
            x_dict[x] = 1
    for y in Y:
        if y in y_dict:
            y_dict[y] += 1
        else:
            y_dict[y] = 1
    
    print(x_dict,y_dict)
    # 0 ~ 9에 대해 두 개 딕셔너리 타입 탐색하면서 공통된 것 추출
    for i in range(9, -1, -1):
        if str(i) in x_dict and str(i) in y_dict:
            if result == '' and i == 0:
                result += '0'
                continue
            result += str(i) * min(x_dict[str(i)], y_dict[str(i)])
    
    return result if result else "-1"