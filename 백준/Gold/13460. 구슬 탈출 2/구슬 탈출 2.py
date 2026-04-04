from collections import deque

n, m = map(int, input().split())
maps = [list(input().strip()) for _ in range(n)]
visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def printing():
    for i in range(n):
        for j in range(m):
            print(maps[i][j],end='')
        print()

def start():
    rx, ry, bx, by = 0,0,0,0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'R':
                rx, ry = i, j
            elif maps[i][j] == 'B':
                bx, by = i, j
    return rx, ry, bx, by

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def move(x, y, dir):
    cnt = 0
    while maps[x + dx[dir]][y + dy[dir]] != '#' and maps[x][y] != 'O':
        x += dx[dir]
        y += dy[dir]
        cnt += 1
    return x, y, cnt

def solve():
    a, b, c, d = start()
    queue = deque([(a, b, c, d, 1)])
    visited[a][b][c][d] = True
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10:
            break

        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, i)
            brx, bry, bcnt = move(bx, by, i)

            if maps[brx][bry] == 'O':
                continue

            if maps[nrx][nry] == 'O':
                return depth

            if nrx == brx and nry == bry:
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    brx -= dx[i]
                    bry -= dy[i]

            if not visited[nrx][nry][brx][bry]:
                visited[nrx][nry][brx][bry] = True
                queue.append((nrx, nry, brx, bry, depth + 1))
    return -1

print(solve())