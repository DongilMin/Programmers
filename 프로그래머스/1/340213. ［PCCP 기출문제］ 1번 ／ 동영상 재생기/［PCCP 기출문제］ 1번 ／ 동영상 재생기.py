def time_to_seconds(time):
    minutes, seconds = map(int, time.split(':'))
    return minutes * 60 + seconds

def second_to_time(second):
    minutes = second // 60
    seconds = second % 60
    return f"{minutes:02d}:{seconds:02d}"

def calculate_time(current_seconds, command, video_len_sec):
    """ 현재 시간(초)과 명령어를 받아 10초를 더하거나 뺀 시간을 반환합니다. """
    if command == "next":
        new_seconds = current_seconds + 10
        # 영상 길이(video_len_sec)를 초과할 수 없도록 max 값을 제한
        return min(video_len_sec, new_seconds)
    
    elif command == "prev":
        new_seconds = current_seconds - 10
        # 0초 미만으로 내려갈 수 없도록 min 값을 제한
        return max(0, new_seconds)

def solution(video_len, pos, op_start, op_end, commands):
    # 계산의 편의를 위해 모든 시간 관련 문자열을 미리 '초' 단위로 변환
    video_len_sec = time_to_seconds(video_len)
    op_start_sec = time_to_seconds(op_start)
    op_end_sec = time_to_seconds(op_end)
    
    # 4. (로직 수정) 계속 변경되는 현재 위치를 추적할 변수 선언
    current_pos_sec = time_to_seconds(pos)

    # 3. (로직 수정) 명령어 처리 '전'에 시작 위치가 오프닝 구간인지 먼저 확인
    if op_start_sec <= current_pos_sec <= op_end_sec:
        current_pos_sec = op_end_sec
        
    # commands 배열에 있는 명령어를 순서대로 처리
    for command in commands:
        # prev/next 명령에 따라 시간 이동 (경계값 처리 포함)
        current_pos_sec = calculate_time(current_pos_sec, command, video_len_sec)
        
        # 3. (로직 수정) 시간 이동 '후'에 바뀐 위치가 오프닝 구간인지 다시 확인
        if op_start_sec <= current_pos_sec <= op_end_sec:
            current_pos_sec = op_end_sec

    # 모든 명령 처리가 끝난 후, 최종 위치(초)를 "mm:ss" 형식으로 변환하여 반환
    return second_to_time(current_pos_sec)









