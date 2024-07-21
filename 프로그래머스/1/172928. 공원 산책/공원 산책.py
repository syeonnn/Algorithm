def solution(park, routes):
    answer = []
    
    h, w = 0,0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                h, w = i, j
    
    dir = {"N": (-1,0), "S": (1,0), "W": (0,-1), "E": (0,1)}

    # 모든 명령 수행 후 놓인 위치 반환
    for route in routes:
        curr_h, curr_w = h, w
        op, n = route.split(" ")
        dh, dw = dir[op]
        
        for _n in range(int(n)): # n번 만큼 이동
            nh = curr_h + dh
            nw = curr_w + dw
        
            # 공원 내부인지, 장애물 없는지 확인
            # 아니라면 해당 명령 무시+다음 명령 수행
            if 0<=nw<len(park[0]) and 0<=nh<len(park) and park[nh][nw] != 'X':
                curr_h, curr_w = nh, nw # 새로운 좌표 업데이트
                flag = True
            else:
                flag = False
                break
                
        if flag:
            h, w = nh, nw
            
    answer = [h,w]
    
    return answer