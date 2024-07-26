def solution(keymap, targets):
    answer = []
    
    key_dict = {}
    for key in keymap:
        for idx, k in enumerate(key):
            if k not in key_dict:
                key_dict[k] = idx + 1
            else:
                key_dict[k] = min(key_dict[k], idx + 1)
    
    for target in targets:
        result = 0
        for char in target:
            if char in key_dict: 
                result += key_dict[char]
            else:
                result = -1
                break
        answer.append(result)
    
    return answer