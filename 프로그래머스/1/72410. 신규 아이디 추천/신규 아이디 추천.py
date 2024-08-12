def solution(new_id):
    answer = ''

    def recommend(new_id):
        new_id = new_id.lower() # 1단계
        
        for char in new_id:
            if char in "~!@#$%^&*()=+[{]}:?,<>/": # 2단계
                new_id = new_id.replace(char, '')
        
        
        while('.'*2 in new_id): # 3단계
            new_id = new_id.replace('.'*2, '.')
        
        if new_id: # 4단계
            if new_id[0] == '.':
                new_id = new_id[1:]
        if new_id:
            if new_id[-1] == '.':
                new_id = new_id[:-1]
                
        if not new_id: # 5단계
            new_id = "a"
        
        if len(new_id) >= 16: # 6단계
            new_id = new_id[0:15]
            if new_id[0] == '.':
                new_id = new_id[1:]
            if new_id[-1] == '.':
                new_id = new_id[:-1]

        if len(new_id) <= 2: # 7단계
            while len(new_id) < 3:
                new_id += new_id[-1]
        
        return new_id
            
    answer = recommend(new_id)
                
    
    return answer