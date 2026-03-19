import math

def solution(n, k):
    answer = []
    numbers = [i for i in range(1, n + 1)]
    k -= 1  
    while n > 0:
        n -= 1
        fact = math.factorial(n)
        index = k // fact
        k %= fact
        
        answer.append(numbers.pop(index))
    return answer