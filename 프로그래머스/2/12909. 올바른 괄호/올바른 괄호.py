def solution(s):
    temp = []

    for bracket in s:
        if bracket == "(":
            temp.append(bracket)
        elif bracket == ")":
            if temp:
                temp.pop()
            else:
                 return False
                
    if temp != []:
        return False
    
    return True # return temp == []