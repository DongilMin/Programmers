from collections import deque

gears = [deque(map(int, input())) for _ in range(4)]

k = int(input())

def rotate_gears(gear_idx, direction):
    # 0: 회전 안함, 1: 시계 방향, -1: 반시계 방향
    move = [0] * 4
    move[gear_idx] = direction

    for i in range(gear_idx, 3):
        if gears[i][2] != gears[i + 1][6]:
            move[i + 1] = -move[i]
        else:
            break

    for i in range(gear_idx, 0, -1):
        if gears[i][6] != gears[i - 1][2]:
            move[i - 1] = -move[i]
        else:
            break

    for i in range(4):
        if move[i] != 0:
            gears[i].rotate(move[i])

for _ in range(k):
    num, dir = map(int, input().split())
    rotate_gears(num - 1, dir)

ans = 0
for i in range(4):
    if gears[i][0] == 1: # 12시 방향이 S극(1)인 경우
        ans += (2 ** i)

print(ans)