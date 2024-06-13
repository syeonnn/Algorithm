# 다 생각안나서... dic으로 개수 비교해서 품... 빙빙 돌아가기😇😆

def solution(v):
    answer = []
    
    # 1. 반드시 두 쌍이 된다는 점을 이용하기 -> 정렬해서 한 쌍 만들기
    
    # x_ = sorted(list(map(lambda x: x[0], v)))
    # y_ = sorted(list(map(lambda y: y[1], v)))
        
    # if x_[0] == x_[1]:
    #     answer.appned(x_[2])
    # elif x_[0] != x_[1]:
    #     answer.append(x_[0])
    # if y_[0] == y_[1]:
    #     answer.append(y_[2])
    # elif y_[0] != y_[1]:
    #     answer.append(y_[0])

    # 2. append와 remove
  
    xs = []
    ys = []

    for x,y in v:
        if x not in xs:
            xs.append(x)
        else:
            xs.remove(x)
        if y not in ys:
            ys.append(y)
        else:
            ys.remove(y)
        
    answer = [xs[0],ys[0]]
    
    return answe
