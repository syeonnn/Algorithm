def solution(s):
    answer = []
    temp = dict()
    
    # 자신의 앞에 같은 글자가 없다면 -1로 표현
    # 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자가 몇 칸 앞에 있는지 표현
    for idx, ch in enumerate(s):
        if ch not in temp.keys():
            answer.append(-1)
        else:
            answer.append(idx - temp[ch])
        temp[ch] = idx
    
    return answer