def solution(today, terms, privacies):
    # 2. terms 리스트를 딕셔너리로 변환하여 쉽게 조회할 수 있도록 함
    # 예: {"A": "6", "B": "12"}
    term_map = {}
    for term in terms:
        name, period = term.split()
        term_map[name] = int(period)

    # 3. 모든 날짜를 '총 일수'로 변환하여 계산을 단순화
    def date_to_days(date_str):
        year, month, day = map(int, date_str.split('.'))
        # 1년 = 12개월 * 28일
        return year * 12 * 28 + (month - 1) * 28 + day

    # 오늘 날짜를 총 일수로 변환
    today_in_days = date_to_days(today)
    
    # 파기할 개인정보의 번호를 저장할 리스트
    remove_list = []
    
    # 각 개인정보를 순회 (인덱스는 1부터 시작)
    for i, privacy in enumerate(privacies):
        agreement_date_str, term_name = privacy.split()
        
        # 개인정보 동의 날짜를 총 일수로 변환
        agreement_in_days = date_to_days(agreement_date_str)
        
        # 유효 기간(달)을 딕셔너리에서 조회
        validity_months = term_map[term_name]
        
        # 만료일을 총 일수로 계산 (동의일 + 유효기간)
        # 모든 달은 28일
        expiration_in_days = agreement_in_days + validity_months * 28
        
        # 4. 파기 조건 확인: 오늘 날짜가 만료일보다 크거나 같다면 파기 대상
        if today_in_days >= expiration_in_days:
            # i는 0부터 시작하므로, 문제의 번호(1부터 시작)에 맞추기 위해 +1
            remove_list.append(i + 1)
            
    # 5. return 값 수정 (정렬이 필요하다면 sorted() 함수 사용 가능)
    return remove_list