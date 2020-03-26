import sys
sys.stdin = open("input73.txt", "rt")
sys.setrecursionlimit(10**6)

def DFS(x, y, h):
    for k in range(4):
        xx = x + dx[k]
        yy = y + dy[k]
        if 0 <= xx < n and 0 <= yy < n and ch[yy][xx] == 0 and board[yy][xx] > h:
            ch[yy][xx] = 1
            DFS(xx, yy, h)


if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    res = -2147000000
    for i in range(100):
        ch = [[0] * n for _ in range(n)]
        cnt = 0
        for y in range(n):
            for x in range(n):
                if board[y][x] > i and ch[y][x] == 0:
                    ch[y][x] = 1
                    cnt += 1
                    DFS(x, y, i)

        res = max(res, cnt)
        if cnt == 0:
            break

    print(res)
