def solution(x, y, n):
    
    dp = [1000002] * 1000001
    dp[x] = 0
    for i in range(x, y + 1):
        if i - n > 0:
            dp[i] = min(dp[i], dp[i - n] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
                    
    return dp[y] if dp[y] < 1000002 else -1