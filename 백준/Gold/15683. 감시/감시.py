from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

cctv = []
for i in range(n):
    for j in range(m):
        if 0 < maps[i][j] < 6:
            cctv.append((maps[i][j], i, j))

# 시계방향 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
modes = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]],
]

ans = 1e9

def get_score(selected_dirs):
    temp = [row[:] for row in maps]

    for i in range(len(cctv)):
        c_type, r, c = cctv[i]
        for d in selected_dirs[i]:
            nx, ny = r, c
            while True:
                nx += dx[d]
                ny += dy[d]
                if not (0 <= nx < n and 0 <= ny < m) or temp[nx][ny] == 6:
                    break
                if temp[nx][ny] == 0:
                    temp[nx][ny] = '#'

    return sum(row.count(0) for row in temp)

def dfs(selected_dirs):
    global ans
    if len(selected_dirs) == len(cctv):
        ans = min(ans, get_score(selected_dirs))
        return

    cctv_type, r, c = cctv[len(selected_dirs)]
    for mode in modes[cctv_type]:
        selected_dirs.append(mode)
        dfs(selected_dirs)
        selected_dirs.pop()

dfs([])
print(ans)