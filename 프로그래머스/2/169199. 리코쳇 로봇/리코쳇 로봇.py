from collections import deque

def BFS(board, start_x, start_y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    # 1. 초기값을 튜플로 감싸서 삽입
    queue = deque([(start_x, start_y, 0)])
    visited = set([(start_x, start_y)]) # 방문 처리용
    
    while queue:
        cx, cy, cnt = queue.popleft()
        
        if board[cx][cy] == 'G':
            return cnt
            
        for i in range(4):
            nx, ny = cx, cy
            while True:
                tx = nx + dx[i]
                ty = ny + dy[i]
                
                if 0 <= tx < len(board) and 0 <= ty < len(board[0]) and board[tx][ty] != 'D':
                    nx, ny = tx, ty
                else:
                    break
            
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, cnt + 1))
    return -1
    
    
def can_go(board, nx, ny):
    return nx >= 0 and ny >= 0 and nx < len(board) and ny < len(board) and board[nx][ny] != 'D' and board[nx][ny] != 'R'

def find_char(board, target):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == target:
                return i, j
    return None

def solution(board):
    s_x, s_y = find_char(board, 'R')
    answer = BFS(board, s_x, s_y)
    return answer