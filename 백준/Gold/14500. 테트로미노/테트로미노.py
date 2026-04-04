n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = 0
max_val = 0
for row in board:
    for val in row:
        if val > max_val:
            max_val = val


def dfs(r, c, idx, total):
    global ans
    if total + max_val * (4 - idx) <= ans:
        return

    if idx == 4:
        ans = max(ans, total)
        return

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
            if idx == 2:
                visited[nr][nc] = True
                dfs(r, c, idx + 1, total + board[nr][nc])
                visited[nr][nc] = False

            visited[nr][nc] = True
            dfs(nr, nc, idx + 1, total + board[nr][nc])
            visited[nr][nc] = False


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False

print(ans)