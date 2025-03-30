def solution(players, m, k):
    answer = 0
    
    curr = [0]*24 # 증설된 서버의 수
    cnt = 0 # 증설 횟수
    
    for i in range(24):
        need = players[i] // m
        
        if curr[i] < need:
            tmp = need - curr[i]
            cnt += tmp
            
            if i+k < 24:
                for j in range(i,i+k):
                    curr[j] += tmp
            else:
                for j in range(i,24):
                    curr[j] += tmp
                    
    # print(curr)
    
                    
    return cnt