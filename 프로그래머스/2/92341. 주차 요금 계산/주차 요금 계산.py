import math

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    parking_log = {}  # 입차 기록 저장
    total_times = {}  # 차량별 누적 시간 저장
    
    for record in records:
        time, car_id, status = record.split()
        h, m = map(int, time.split(':'))
        minutes = h * 60 + m
        
        if status == "IN":
            parking_log[car_id] = minutes
        else:
            total_times[car_id] = total_times.get(car_id, 0) + (minutes - parking_log.pop(car_id))
            
    # 출차 기록이 없는 차량 처리 (23:59 출차 간주)
    last_time = 23 * 60 + 59
    for car_id, start_time in parking_log.items():
        total_times[car_id] = total_times.get(car_id, 0) + (last_time - start_time)
        
    # 요금 계산 및 차량 번호 순 정렬
    answer = []
    for car_id in sorted(total_times.keys()):
        time = total_times[car_id]
        if time <= base_time:
            fee = base_fee
        else:
            fee = base_fee + math.ceil((time - base_time) / unit_time) * unit_fee
        answer.append(fee)
        
    return answer