from collections import deque

def solution(prices):
    answer = []
    
    price_chart = deque(prices)
    while price_chart:
        price = price_chart.popleft()
        flag = False
        cnt = 0
        
        for cmp in price_chart:
            cnt += 1
            if price > cmp:
                answer.append(cnt)
                flag = True
                break
                
        if not flag:
            answer.append(cnt)
    
    return answer