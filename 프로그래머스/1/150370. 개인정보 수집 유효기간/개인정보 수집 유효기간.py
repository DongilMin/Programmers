def solution(today, terms, privacies):
    # 데이터 분류
    # terms에서 날짜 더하고
    # 오늘 날짜와 비교
    # 삭제될 데이터면 수집
    term_map = {}
    for term in terms:
        name, peroid = term.split()
        term_map[name] = int(peroid)
    
    def date_to_days(date_str):
        year, month, day = map(int, date_str.split('.'))
        return year * 12 * 28 + (month - 1) * 28 + day

    today_in_days = date_to_days(today)
    
    remove_list = []
    
    for i, privacy in enumerate(privacies):
        date, name = privacy.split()
        
        agreement_date = date_to_days(date)
        validation_months = term_map[name]
        expire_date = agreement_date + validation_months * 28
        
        if today_in_days >= expire_date:
            remove_list.append(i + 1)
        
    return remove_list
        
        
        