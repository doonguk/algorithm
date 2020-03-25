import sys

sys.stdin = open("input70.txt", "rt")

def DFS(x, y):
    global cnt
    board[y][x] = 0
    cnt += 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and board[yy][xx] == 1:
            DFS(xx, yy)


if __name__ == '__main__':
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    res = list()
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    for y in range(n):
        for x in range(n):
            if board[y][x] == 1:
                cnt = 0
                DFS(x, y)
                res.append(cnt)
    print(len(res))
    for v in sorted(res):
        print(v)