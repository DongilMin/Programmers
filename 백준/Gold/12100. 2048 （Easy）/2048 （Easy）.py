N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def move(line):
    """한 행(리스트)을 왼쪽으로 밀어 합친 결과를 반환"""
    new_line = [n for n in line if n != 0] # 0 제외 숫자만 추출
    res = []
    skip = False
    for i in range(len(new_line)):
        if skip:
            skip = False
            continue
        if i + 1 < len(new_line) and new_line[i] == new_line[i+1]:
            res.append(new_line[i] * 2)
            skip = True # 합쳐졌으므로 다음 숫자는 건너뜀
        else:
            res.append(new_line[i])
    return res + [0] * (N - len(res))

def dfs(n, arr):
    global ans
    ans = max(ans, max(map(max, arr)))
    if n == 5:
        return

    # 1. 좌측 이동: 행 그대로 move
    dfs(n + 1, [move(row) for row in arr])

    # 2. 우측 이동: 행을 뒤집어서 move 후 다시 뒤집음
    dfs(n + 1, [move(row[::-1])[::-1] for row in arr])

    # 3. 상측 이동: 열을 추출해서 move 후 다시 열로 재배치
    # zip(*arr)은 열을 튜플로 반환하므로 list(col)로 변환 필요
    transposed_up = [move(list(col)) for col in zip(*arr)]
    dfs(n + 1, [list(row) for row in zip(*transposed_up)])

    # 4. 하측 이동: 열을 추출해 뒤집어서 move 후 다시 뒤집고 열로 재배치
    transposed_down = [move(list(col)[::-1])[::-1] for col in zip(*arr)]
    dfs(n + 1, [list(row) for row in zip(*transposed_down)])

ans = 0
dfs(0, board)
print(ans)