import sys

sys.stdin = open("input92.txt", "rt")


def DFS(x, y):
    ch[y][x] = 1
    if y == 0:
        print(x)
    else:
        if x-1 >= 0 and board[y][x-1] == 1 and ch[y][x-1] == 0:
            DFS(x-1, y)
        elif x+1 < 10 and board[y][x+1] == 1 and ch[y][x+1] == 0:
            DFS(x+1, y)
        else:
            DFS(x, y-1)


if __name__ == '__main__':
    board = [list(map(int, input().split())) for _ in range(10)]

    ch = [[0] * 10 for _ in range(10)]

    for i in range(10):
        if board[9][i] == 2:
            DFS(i, 9)