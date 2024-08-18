def solution(numbers, hand):
    answer = ''
    
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # * 0 #
    
    nums = {'*' : [0,0], '0': [1,0], '#': [2,0], '7': [0,1], '8': [1,1], '9': [2,1], '4': [0,2], '5': [1,2], '6': [2,2], '1': [0,3], '2': [1,3], '3': [2,3]}
    
    left_curr, right_curr = [0,0], [0,0]
    
    for n in numbers:
        n = str(n)
        if n in ['1','4','7']:
            answer += 'L'
            left_curr = nums[n]
        elif n in ['3','6','9']:
            answer += 'R'
            right_curr = nums[n]
        else:
            left_dis = abs(left_curr[0] - nums[n][0]) + abs(left_curr[1] - nums[n][1])
            right_dis = abs(right_curr[0] - nums[n][0]) + abs(right_curr[1] - nums[n][1])
            if left_dis < right_dis:
                answer += 'L'
                left_curr = nums[n]
            elif right_dis < left_dis:
                answer += 'R'
                right_curr = nums[n]
            else:
                ans_temp = 'R' if hand == 'right' else 'L'
                answer += ans_temp
                if hand == 'right':
                    right_curr = nums[n]
                else:
                    left_curr = nums[n]

            
    return answer