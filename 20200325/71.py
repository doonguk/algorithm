import sys
from collections import deque

sys.stdin = open("input70.txt", "rt")


def BFS(a, b):
    dQ = deque()
    dQ.append((a, b))
    board[b][a] = 0
    cnt = 1
    while dQ:
        x, y = dQ.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and board[yy][xx] == 1:
                dQ.append((xx, yy))
                cnt += 1
                board[yy][xx] = 0
    return cnt


if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    res = list()
    for y in range(n):
        for x in range(n):
            if board[y][x] == 1:
                res.append(BFS(x, y))
    print(len(res))
    for v in sorted(res):
        print(v)
