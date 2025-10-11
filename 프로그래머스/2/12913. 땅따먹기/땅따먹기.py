def solution(land):

    for i in range(1, len(land)):

        for j in range(len(land[0])):
            prev_row = land[i-1]
            max_from_prev = max(prev_row[:j] + prev_row[j+1:])
            
            land[i][j] += max_from_prev
            
    return max(land[-1])