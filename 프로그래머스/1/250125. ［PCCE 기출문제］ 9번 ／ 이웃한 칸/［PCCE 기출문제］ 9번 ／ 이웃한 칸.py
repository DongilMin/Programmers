def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

def solution(board, h, w):
    n = len(board)
    count = 0
    dh = (0, 1, -1, 0)
    dw = (1, 0, 0, -1)
    
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if not in_range(h_check, w_check, n):
            continue
        if board[h][w] == board[h_check][w_check]:
            count += 1
    return count
        