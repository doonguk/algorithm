import sys
from collections import deque

sys.stdin = open("input67.txt", "rt")

if __name__ == '__main__':
    a = [list(map(int, input().split())) for _ in range(7)]
    dis = [[0] * 7 for _ in range(7)]
    dQ = deque()
    dQ.append((0, 0))
    a[0][0] = 1
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    while dQ:
        size = len(dQ)
        tmp = dQ.popleft()
        for i in range(4):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            if 0 <= x < 7 and 0 <= y < 7 and a[y][x] == 0:
                a[y][x] = 1
                dis[y][x] = dis[tmp[1]][tmp[0]] + 1
                dQ.append((x, y))

    if dis[6][6] == 0:
        print(-1)
    else:
        print(dis[6][6])
