def solution(book_time):
    time_table = [0] * 1500
    
    for start, end in book_time:
        
        s_h, s_m = map(int, start.split(':'))
        start_time = s_h * 60 + s_m

        e_h, e_m = map(int, end.split(':'))
        end_time = e_h * 60 + e_m + 10
        
        time_table[start_time] += 1
        time_table[end_time] -= 1
        
        
    max_rooms = 0
    current_rooms = 0
    
    for rooms in time_table:
        current_rooms += rooms
        if current_rooms > max_rooms:
            max_rooms = current_rooms
    
    return max_rooms