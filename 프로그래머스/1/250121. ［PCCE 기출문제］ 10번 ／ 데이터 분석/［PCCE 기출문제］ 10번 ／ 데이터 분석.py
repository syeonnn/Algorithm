def solution(data, ext, val_ext, sort_by):
    answer = []
    data_dict = []
    
    for row in data:
        [code, date, maximum, remain] = row
        data_temp = {}
        data_temp['code'] = code
        data_temp['date'] = date
        data_temp['maximum'] = maximum
        data_temp['remain'] = remain
        data_dict.append(data_temp)
    
    # data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후, 
    extracted_data = [ d for d in data_dict if d[ext] < val_ext]
    # sort_by에 해당하는 값을 기준으로 오름차순으로 정렬
    extracted_data.sort(key = lambda x : (x[sort_by]))
    
    for sorted_data in extracted_data:
        answer.append(list(sorted_data.values()))

    return answer