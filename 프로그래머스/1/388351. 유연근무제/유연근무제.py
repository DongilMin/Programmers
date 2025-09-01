def time_to_minutes(t):
    """1055 같은 숫자 시간을 총 분으로 변환합니다."""
    
    # 몫 연산자(//)로 시간 부분을 구함 (1055 // 100 -> 10)
    hours = t // 100
    
    # 나머지 연산자(%)로 분 부분을 구함 (1055 % 100 -> 55)
    minutes = t % 100
    
    return hours * 60 + minutes

def solution(schedules, timelogs, startday):
    answer = 0
    for i, records in enumerate(timelogs):
        limit_time = time_to_minutes(schedules[i]) + 10
        for j, record in enumerate(records):
            current_day = (startday + j) % 7
            
            if current_day in {0, 6}:
                continue
            
            record_time = time_to_minutes(record)
            if record_time > limit_time:
                break
        else:
            answer += 1
            
    return answer