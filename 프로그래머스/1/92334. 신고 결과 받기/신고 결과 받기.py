def solution(id_list, report, k):
    answer = []
    
    id_len = len(id_list)
    name_to_idx = {user_id: i for i, user_id in enumerate(id_list)}
    report_set = set(report)
    
    report_record = [0] * id_len
    for r in report_set:
        people, target = r.split()
        report_record[name_to_idx[target]] += 1
            
    block_list = [user for user, count in zip(id_list, report_record) if count >= k ]
    
    mail_counts = [0] * len(id_list)
    for r in report_set:
        people, target = r.split()
        if target in block_list:
            mail_counts[name_to_idx[people]] += 1
    
    return mail_counts