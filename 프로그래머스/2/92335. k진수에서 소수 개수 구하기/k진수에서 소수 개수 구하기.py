def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 ==0:
        return False
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
            
    return True

def func(n, k):
    result = ""
    while n > 0:
        result = str(n % k) + result
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
            