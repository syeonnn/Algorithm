def solution(sizes):

    a = [min(w,h) for [w,h] in sizes]
    b = [max(w,h) for [w,h] in sizes]
    
    return max(a) * max(b)