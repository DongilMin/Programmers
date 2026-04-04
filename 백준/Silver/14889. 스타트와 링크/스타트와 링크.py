n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
ans = 1e9  # 아주 큰 값으로 초기화

def calculate():
    start_score = 0
    link_score = 0
    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:
                start_score += s[i][j]
            elif not visited[i] and not visited[j]:
                link_score += s[i][j]
    return abs(start_score - link_score)

def dfs(idx, cnt):
    global ans
    if cnt == n // 2:
        ans = min(ans, calculate())
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(i + 1, cnt + 1)
            visited[i] = False

dfs(0, 0)
print(ans)