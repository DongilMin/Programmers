def solution(board):
    
    answer = 0
    # 1x1 보드 등 초기 최댓값 설정
    for row in board:
        if max(row) > 0:
            answer = 1
            break

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                answer = max(answer, board[i][j])

    return answer ** 2