n, m, h = map(int, input().split())

board = [[False] * (n + 1) for _ in range(h + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    board[a][b] = True

candidates = []
for i in range(1, h + 1):
    for j in range(1, n):
        if not board[i][j] and not board[i][j - 1] and not board[i][j + 1]:
            candidates.append((i, j))

def get_wrong_count():
    cnt = 0
    for start in range(1, n + 1):
        now = start
        for j in range(1, h + 1):
            if board[j][now]:
                now += 1
            elif board[j][now - 1]:
                now -= 1
        if now != start:
            cnt += 1
    return cnt

def dfs(cnt, idx, limit):
    wrong = get_wrong_count()
    
    if wrong == 0:
        print(cnt)
        exit()
        
    if wrong > (limit - cnt) * 2:
        return
        
    if cnt == limit:
        return

    for k in range(idx, len(candidates)):
        r, c = candidates[k]
        if not board[r][c - 1] and not board[r][c + 1]:
            board[r][c] = True
            dfs(cnt + 1, k + 1, limit)
            board[r][c] = False

if get_wrong_count() == 0:
    print(0)
    exit()

for limit in range(1, 4):
    dfs(0, 0, limit)

print(-1)