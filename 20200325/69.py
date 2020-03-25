import sys

sys.stdin = open("input69.txt", "rt")


def DFS(L):
    global cnt
    if L == e:
        cnt += 1
    else:
        x, y = L
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and board[y][x] < board[yy][xx]:
                DFS((xx, yy))


if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    s = (0, 0)
    e = (0, 0)
    for y, a in enumerate(board):
        for x, b in enumerate(a):
            if b < board[s[1]][s[0]]:
                s = (x, y)
            if b > board[e[1]][e[0]]:
                e = (x, y)
    cnt = 0
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    DFS(s)
    print(cnt)
