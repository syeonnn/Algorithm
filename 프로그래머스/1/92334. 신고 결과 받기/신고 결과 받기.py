from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    report_dict = defaultdict(set)
        
    for r in report:
        a, b = r.split(" ")
        report_dict[b].add(a)
            
    for person, getReport in report_dict.items():
        if len(getReport) >= k:
            # person을 신고한 내역이 있는 사람들에 대해 메일 전송
            for who in getReport:
                answer[id_list.index(who)] += 1
            
    return answer #  각 유저별로 처리 결과 메일을 받은 횟수