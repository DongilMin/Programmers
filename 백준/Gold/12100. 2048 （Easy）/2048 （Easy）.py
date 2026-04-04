n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def move(line):
    new_line = [a for a in line if a != 0]
    res = []
    skip = False
    for i in range(len(new_line)):
        if skip:
            skip = False
            continue
        if i + 1 < len(new_line) and new_line[i] == new_line[i + 1]:
            res.append(new_line[i] * 2)
            skip = True
        else:
            res.append(new_line[i])
    return res + [0] * (n - len(res))

def dfs(cnt, arr):
    global ans
    ans = max(ans, max(map(max, arr)))
    if cnt == 5:
        return

    # 좌측
    dfs(cnt + 1, [move(row) for row in arr])

    # 우측
    dfs(cnt + 1, [move(row[::-1])[::-1] for row in arr])

    # 상측
    t_up = [move(list(col)) for col in zip(*arr)]
    dfs(cnt + 1, [list(row) for row in zip(*t_up)])

    # 하측
    t_d = [move(list(col)[::-1])[::-1] for col in zip(*arr)]
    dfs(cnt + 1, [list(row) for row in zip(*t_d)])

ans = 0
dfs(0, board)
print(ans)