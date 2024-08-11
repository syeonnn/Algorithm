def solution(s):
    numbers = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    
    answer = s
    for key, value in numbers.items():
        answer = answer.replace(key, value)
        
    # answer = ''
    # temp = ''
    # for a in s:
    #     if a.isdigit():
    #         answer += a
    #     else:
    #         temp += a
    #         if temp in numbers:
    #             answer += numbers[temp]
    #             temp = ''

    return int(answer)