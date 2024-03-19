def solution(number, k):
    answer = ''

    stack = []
    
    for num in number:
        while  stack and k > 0 and num > stack[-1]:
            stack.pop()
            k-=1
            
        stack.append(num)
 
    for a in stack[:len(stack)-k]:
        answer+=a
    
    return answer

