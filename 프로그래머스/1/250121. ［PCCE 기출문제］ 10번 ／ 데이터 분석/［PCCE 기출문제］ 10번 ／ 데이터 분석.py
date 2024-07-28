def solution(data, ext, val_ext, sort_by):
    answer = []
    # !!반복적으로 등장하는 문자열은 배열, 인덱스 활용하기!!
    by = ['code', 'date', 'maximum', 'remain']
    
    # data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후, 
    extracted_data = [ row for row in data if row[by.index(ext)] < val_ext]
    # sort_by에 해당하는 값을 기준으로 오름차순으로 정렬
    answer = sorted(extracted_data, key = lambda x : (x[by.index(sort_by)]))

    return answer