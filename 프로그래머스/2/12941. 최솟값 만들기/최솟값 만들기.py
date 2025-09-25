def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    min_sum = 0
    
    for i in range(len(A)):
        min_sum += A[i] * B[i]
        
    return min_sum