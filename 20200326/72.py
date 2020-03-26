import sys
from collections import deque
sys.stdin = open("input72.txt", "rt")

def BFS(x, y):
    board[y][x] = 0
    dQ = deque()
    dQ.append((x, y))
    while dQ:
        a, b = dQ.popleft()
        for i in range(8):
            xx = a + dx[i]
            yy = b + dy[i]
            if 0 <= xx < n and 0 <= yy < n and board[yy][xx] == 1:
                board[yy][xx] = 0
                dQ.append((xx, yy))



if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    cnt = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] == 1:
                cnt += 1
                BFS(x, y)
    print(cnt)