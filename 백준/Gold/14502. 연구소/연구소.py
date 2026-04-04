from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
virus = [(i, j) for i in range(n) for j in range(m) if maps[i][j] == 2]

ans = 0

def bfs():
    cnt = 0
    tmp_maps = [row[:] for row in maps]

    queue = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for v in virus:
        a, b = v
        queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and tmp_maps[nx][ny] == 0:
                tmp_maps[nx][ny] = 2
                queue.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if tmp_maps[i][j] == 0:
                cnt += 1

    return cnt

def make_wall(cnt, r, c):
    global ans
    if cnt == 3:
        ans = max(ans, bfs())
        return

    # 시작 행(r)부터 마지막 행까지 순회
    for i in range(r, n):
        start_c = c if i == r else 0
        for j in range(start_c, m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                # 다음 칸부터 탐색하도록 전달 (j + 1)
                make_wall(cnt + 1, i, j + 1)
                maps[i][j] = 0

make_wall(0, 0, 0)
print(ans)