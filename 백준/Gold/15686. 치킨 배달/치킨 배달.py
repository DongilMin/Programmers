n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

stores = []
homes = []
ans = 1e9
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            homes.append((i, j))
        elif board[i][j] == 2:
            stores.append((i, j))

def get_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def solve(selected_stores):
    #print(f"selected store list is {selected_stores}")
    total_dist = 0
    for home in homes:

        r1, c1 = home
        home_dist = 1e9
        for store in selected_stores:
            r2, c2 = store
            home_dist = min(home_dist, get_dist(r1, c1, r2, c2))
        total_dist += home_dist
        #print(f"home:{home} and dist:{home_dist}")
    return total_dist

def dfs(selected_stores, idx, limit):
    global ans
    if len(selected_stores) == limit:
        curr_dist = solve(selected_stores)
        ans = min(ans, curr_dist)
        return

    for i in range(idx, len(stores)):
        selected_stores.append(stores[i])
        dfs(selected_stores, i + 1, limit)
        selected_stores.pop()

for i in range(1, m + 1):
    dfs([], 0, i)

print(ans)