def solution(answers):
    answer = []
    m1 = [1, 2, 3, 4, 5]
    m2 = [2, 1, 2, 3, 2, 4, 2, 5]
    m3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = [0,0,0]
    
    for i,a in enumerate(answers):
        if a == m1[i%len(m1)]: result[0] += 1
        if a == m2[i%len(m2)]: result[1] += 1
        if a == m3[i%len(m3)]: result[2] += 1

    for i,r in enumerate(result):
        if r == max(result):
            answer.append(i+1)
            
    return answer