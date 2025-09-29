def solution(elements):

    n = len(elements)

    extended_elements = elements * 2
    
    unique_sums = set()
    
    for length in range(1, n + 1):
        for start in range(n):
            sub_sequence = extended_elements[start : start + length]
            current_sum = sum(sub_sequence)
            
            unique_sums.add(current_sum)
            
    return len(unique_sums)