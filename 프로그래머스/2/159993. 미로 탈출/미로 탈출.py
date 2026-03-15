from collections import deque

def BFS(start_x, start_y, maps, destination):
    rows = len(maps)
    cols = len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    
    queue = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y, dist = queue.popleft()
        if maps[x][y] == destination:
            return dist, x, y
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < rows and 0 <= ny < cols:
                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))
    return -1, -1, -1
        

def find_char(maps, target):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == target:
                return i, j
    return None
    
def solution(maps):
    s_x, s_y = find_char(maps, 'S')
    
    dist_to_lever, l_x, l_y = BFS(s_x, s_y, maps, 'L')

    if dist_to_lever == -1:
        return -1
    
    dist_to_exit, a, b = BFS(l_x, l_y, maps, 'E')
    
    if dist_to_exit == -1:
        return -1
    return dist_to_exit + dist_to_lever

