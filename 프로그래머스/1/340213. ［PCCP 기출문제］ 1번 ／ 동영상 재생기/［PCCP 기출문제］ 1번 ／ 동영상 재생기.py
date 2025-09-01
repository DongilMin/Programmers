def time_to_seconds(time):
    minutes, seconds = map(int, time.split(':'))
    return minutes * 60 + seconds

def seconds_to_time(second):
    minutes = second // 60
    seconds = second % 60
    
    return f"{minutes:02d}:{seconds:02d}"

def calculate_time(time, command, video_len):
    if command == "next":
        time += 10
        return (min(time, video_len))
    else:
        time -= 10
        return (max(time, 0))

def solution(video_len, pos, op_start, op_end, commands):
    
    start_pos_seconds = time_to_seconds(op_start)
    end_pos_seconds = time_to_seconds(op_end)
    video_seconds = time_to_seconds(video_len)
    current_seconds = time_to_seconds(pos)
    
    if start_pos_seconds <= current_seconds <= end_pos_seconds:
        current_seconds = end_pos_seconds
    
    for command in commands:
        current_seconds = calculate_time(current_seconds, command, video_seconds)
        print(current_seconds)
        if start_pos_seconds <= current_seconds <= end_pos_seconds:
            current_seconds = end_pos_seconds
            
    return seconds_to_time(current_seconds)









