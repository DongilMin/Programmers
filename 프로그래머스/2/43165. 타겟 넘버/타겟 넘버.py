from collections import deque

def solution(numbers, target):
    leaves = [0] # 시작 합계
    for num in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + num)
            tmp.append(parent - num)
        leaves = tmp
    return leaves.count(target)