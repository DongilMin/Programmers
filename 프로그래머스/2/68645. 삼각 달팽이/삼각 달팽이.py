def solution(n):
    # n x n 크기의 2차원 배열 초기화 (삼각형 모양)
    matrix = [[0] * i for i in range(1, n + 1)]
    y, x = -1, 0  # 시작 위치 (첫 번째 이동이 아래쪽이므로 y를 -1로 설정)
    num = 1
    
    for i in range(n): # 방향 전환 횟수
        for j in range(i, n): # 각 방향에서 채울 숫자의 개수
            # 아래쪽 이동
            if i % 3 == 0:
                y += 1
            # 오른쪽 이동
            elif i % 3 == 1:
                x += 1
            # 대각선 위쪽 이동
            else:
                y -= 1
                x -= 1
            
            matrix[y][x] = num
            num += 1
            
    # 2차원 배열을 1차원으로 합치기
    return [val for row in matrix for val in row]