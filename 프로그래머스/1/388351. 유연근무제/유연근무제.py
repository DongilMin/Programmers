def time_to_minutes(t):
    """1055 같은 숫자 시간을 총 분으로 변환합니다."""
    
    # 몫 연산자(//)로 시간 부분을 구함 (1055 // 100 -> 10)
    hours = t // 100
    
    # 나머지 연산자(%)로 분 부분을 구함 (1055 % 100 -> 55)
    minutes = t % 100
    
    return hours * 60 + minutes

def solution(schedules, timelogs, startday):
    answer = 0
    
    # timelogs에서 한 사람(person_logs)의 기록을 순서대로 가져옴
    # i는 그 사람의 인덱스
    for i, person_logs in enumerate(timelogs):
        
        # 한 사람의 출근 기록(arrived_time)을 하루씩(j) 확인
        for j, arrived_time in enumerate(person_logs):
            
            # 1. (수정) 괄호를 사용하여 올바른 요일 계산
            # 2. (개선) 변수로 분리하고 'in'을 사용하여 가독성 향상
            current_day = (startday + j) % 7
            
            # 주말(토요일=6, 일요일=0)인 경우 출근 여부를 확인하지 않음
            if current_day in {0, 6}:
                continue
            
            # 스케줄 시간 + 10분(지각 허용 시간)보다 늦게 도착했다면
            schedule_min = time_to_minutes(schedules[i])
            arrived_min = time_to_minutes(arrived_time)

            if arrived_min > schedule_min + 10:
                # 3. (개선) 이 사람은 보상 대상이 아니므로 안쪽 for문을 중단
                break
        
        # 4. (개선) for-else 구문 사용
        # 안쪽 for문이 break로 중단되지 않았다면 (즉, 한번도 지각 안했다면)
        # else 블록이 실행됨
        else:
            answer += 1
            
    return answer