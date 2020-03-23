import sys
from collections import deque

sys.stdin = open("input66.txt", "rt")

if __name__ == '__main__':
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    ch = [[0] * n for _ in range(n)]
    dQ = deque()
    dQ.append((n // 2, n // 2))
    tot = a[n // 2][n // 2]
    ch[n//2][n//2] = 1
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    L = 0

    while True:
        if L == n // 2:
            break
        size = len(dQ)
        for i in range(size):
            tmp = dQ.popleft()
            for j in range(4):
                x = tmp[0] + dx[j]
                y = tmp[1] + dy[j]
                if ch[y][x] == 0:
                    tot += a[y][x]
                    ch[y][x] = 1
                    dQ.append((x, y))
        L += 1
    print(tot)
