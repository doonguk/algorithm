import sys

sys.stdin = open("input93.txt", "rt")


def DFS(x, y, l):
    if board[y][x] == 2:
        if tmp[y][x] == 0:
            tmp[y][x] = l
        else:
            if tmp[y][x] > l:
                tmp[y][x] = l
    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < n and ch[yy][xx] == 0:
                ch[yy][xx] = 1
                DFS(xx, yy, l + abs(x - xx) + abs(y - yy))
                ch[yy][xx] = 0


if __name__ == '__main__':
    print(ord('A'))