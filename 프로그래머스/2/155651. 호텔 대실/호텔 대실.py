def solution(book_time):
    time_table = [0] * 1500
    
    for start, end in book_time:
        
        s_h, s_m = map(int, start.split(':'))
        s_time = s_h * 60 + s_m
        
        e_hh, e_mm = map(int, end.split(':'))
        e_time = e_hh * 60 + e_mm + 10
        
        time_table[s_time] += 1
        time_table[e_time] -= 1
        
    max_rooms = 0
    current_rooms = 0
    for i in range(len(time_table)):
        current_rooms += time_table[i]
        if current_rooms > max_rooms:
            max_rooms = current_rooms

    return max_rooms