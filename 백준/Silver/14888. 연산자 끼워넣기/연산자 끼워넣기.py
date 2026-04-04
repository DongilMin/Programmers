n = int(input())
nums = list(map(int, input().split()))
op_count = list(map(int, input().split()))

max_ans = -1e9  # -10억
min_ans = 1e9  # 10억


def dfs(idx, res, add, sub, mul, div):
    global max_ans, min_ans

    # 종료 조건: 모든 숫자를 다 계산에 사용했을 때
    if idx == n:
        max_ans = max(max_ans, res)
        min_ans = min(min_ans, res)
        return

    # 각 연산자가 남아있다면 시도
    if add > 0:
        dfs(idx + 1, res + nums[idx], add - 1, sub, mul, div)
    if sub > 0:
        dfs(idx + 1, res - nums[idx], add, sub - 1, mul, div)
    if mul > 0:
        dfs(idx + 1, res * nums[idx], add, sub, mul - 1, div)
    if div > 0:
        # 나눗셈 조건: 음수를 양수로 나눌 때의 처리 (C++14 기준)
        if res < 0:
            dfs(idx + 1, -(-res // nums[idx]), add, sub, mul, div - 1)
        else:
            dfs(idx + 1, res // nums[idx], add, sub, mul, div - 1)


# 첫 번째 숫자를 시작값으로 넣고, 인덱스는 1부터 시작
dfs(1, nums[0], op_count[0], op_count[1], op_count[2], op_count[3])

print(int(max_ans))
print(int(min_ans))