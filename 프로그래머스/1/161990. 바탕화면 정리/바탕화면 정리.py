def solution(wallpaper):
    answer = []
    
    # 드래그 시작점 lux, luy
    # 범위 설정 넉넉하게 하기!!!!!
    lux, luy = 51, 51
    # 드래그 끝점 rdx, rdy
    rdx, rdy = 0, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                print(i, j)
                lux, luy = min(lux, i), min(luy, j)
                rdx, rdy = max(rdx, i), max(rdy, j)
    
    answer = [lux, luy, rdx+1, rdy+1]
    
    # 끝점은 좌표 값 + 1
    return answer