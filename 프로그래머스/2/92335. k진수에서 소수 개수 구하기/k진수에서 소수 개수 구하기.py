def is_prime(n):
    # 1은 소수가 아님
    if n < 2:
        return False
    
    # 2는 유일한 짝수 소수
    if n == 2:
        return True
    
    # 짝수는 2를 제외하고 소수가 아님
    if n % 2 == 0:
        return False
    
    # 3부터 n의 제곱근까지 홀수만 확인 (훨씬 효율적)
    # n의 약수는 항상 sqrt(n)을 기준으로 쌍을 이루므로, sqrt(n)까지만 확인하면 충분함
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2  # 홀수만 검사
        
    return True

def func(n, k):
    result = ""
    while n > 0:
        result = str(n%k) + result
        n //= k
    return result


def solution(n, k):
    
    s = func(n, k)
    arr = s.split('0')
    
    result = 0
    for num in arr:
        if num and is_prime(int(num)):
            result += 1
    return result
            