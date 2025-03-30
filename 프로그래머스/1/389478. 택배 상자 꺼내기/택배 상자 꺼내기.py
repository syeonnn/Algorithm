def solution(n, w, num):


    MAX_ROW = n // w+1
    boxes = []
        
    for row in range(MAX_ROW):
        list = [row*w + i if row*w + i <= n else 0 for i in range(1, w+1)]
        if row % 2 == 1:
            list.reverse()
        boxes.append(list)

    for r in range(len(boxes)):
        for c in range(w):
            if boxes[r][c] == num:
                answer = 0
                while r < MAX_ROW and boxes[r][c]: # 0아닌 상단 박스들에 대해
                    r += 1
                    answer += 1
                return answer
    
    return 0