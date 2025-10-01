from collections import deque

def solution(maps):

    n = len(maps)
    m = len(maps[0])
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # BFS를 위한 큐(queue) 생성
    # 시작 위치 (0, 0)와 시작점까지의 거리 1을 큐에 추가
    queue = deque([(0, 0, 1)])
    
    # 시작점 방문 처리 (다시 방문하지 않기 위해 벽으로 만듦)
    maps[0][0] = 0
    
    while queue:
        x, y, distance = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return distance
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 다음 위치가 맵 범위 안에 있고, 벽이 아닌 경우
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                # 다음 위치를 방문 처리
                maps[nx][ny] = 0
                # 다음 위치와 새로운 거리를 큐에 추가
                queue.append((nx, ny, distance + 1))
                
    # 큐가 비워질 때까지 도착점에 도달하지 못했으면 -1 반환
    return -1