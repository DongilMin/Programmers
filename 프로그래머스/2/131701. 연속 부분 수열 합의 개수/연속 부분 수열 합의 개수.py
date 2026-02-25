def solution(elements):
    n = len(elements)
    extended_ele = elements * 2
    unique_sum = set()

    for length in range(1, n + 1):
        for start in range(n):
            add_sum = sum(extended_ele[start : start + length])
            unique_sum.add(add_sum)
            
    return len(unique_sum)