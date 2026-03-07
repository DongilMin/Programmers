def solution(dirs):
    move = {'U': (1, 0), 'D': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
    cx, cy = 0, 0
    paths = set()
    
    for d in dirs:
        dx, dy = move[d]
        nx, ny = cx + dx, cy + dy
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            paths.add((cx, cy, nx, ny))
            paths.add((nx, ny, cx, cy))
            cx, cy = nx, ny
    return len(paths)//2