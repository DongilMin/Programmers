n, m, h = map(int, input().split())
maps = [[0] * (n + 1) for _ in range(h + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    maps[a][b] = True

candidates = []
for i in range(1, h + 1):
    for j in range(1, n):
        if not maps[i][j] and not maps[i][j - 1] and not maps[i][j + 1]:
            candidates.append((i, j))

def count_wrong():
    cnt = 0
    for start in range(1, n + 1):
        now = start
        for j in range(1, h + 1):
            if maps[j][now]:
                now += 1
            elif maps[j][now - 1]:
                now -= 1
        if now != start:
            cnt += 1
    return cnt

def dfs(cnt, idx, limit):
    wrong = count_wrong()

    if wrong == 0:
        print(cnt)
        exit()
    if wrong > (limit - cnt) * 2:
        return

    if cnt == limit:
        return

    for k in range(idx, len(candidates)):
        r, c = candidates[k]
        if not maps[r][c - 1] and not maps[r][c + 1]:
            maps[r][c] = True
            dfs(cnt + 1, k + 1, limit)
            maps[r][c] = False

if count_wrong() == 0:
    print(0)
    exit()

for limit in range(1, 4):
    dfs(0, 0, limit)

print(-1)