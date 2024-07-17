def solution(board, h, w):
    answer = 0
    target = board[h][w]
    
    for dh,dw in [(-1,0), (1,0), (0,1), (0,-1)]:
        nh, nw = h + dh, w + dw
        if 0 <= nh < len(board) and 0 <= nw < len(board):
            if board[nh][nw] == target:
                answer += 1
            
    return answer