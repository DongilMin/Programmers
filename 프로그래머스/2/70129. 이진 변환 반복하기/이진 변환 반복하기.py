def solution(s):
    cnt = 0
    removed_zeros = 0
    while s != "1":

        removed_zeros += s.count('0')
        a = len(s) - s.count('0')
        b = bin(a)[2:]
        s = b
        cnt += 1
    return [cnt, removed_zeros]