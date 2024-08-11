def solution(price, money, count):
    need = 0
    
    for i in range(1,count+1):
        need += price*i

    return need-money if money < need else 0 # 모자란 금액