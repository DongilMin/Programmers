n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cctv = [(board[i][j], i, j) for i in range(n) for j in range(m) if 1 <= board[i][j] <= 5]

# 상(0), 우(1), 하(2), 좌(3) - 시계 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

modes = [
    [],
    [[0], [1], [2], [3]], # 1번: 한 방향
    [[0, 2], [1, 3]],     # 2번: 상하 / 좌우
    [[0, 1], [1, 2], [2, 3], [3, 0]], # 3번: 직각
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], # 4번: 세 방향
    [[0, 1, 2, 3]]        # 5번: 네 방향
]

ans = 1e9

def get_score(selected_dirs):
    temp = [row[:] for row in board]

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
    if len(cctv) == len(selected_dirs):
        ans = min(ans, get_score(selected_dirs))
        return

    curr_idx = len(selected_dirs)
    c_type, r, c = cctv[curr_idx]

    for d in modes[c_type]:
        selected_dirs.append(d)
        dfs(selected_dirs)
        selected_dirs.pop()

dfs([])
print(ans)