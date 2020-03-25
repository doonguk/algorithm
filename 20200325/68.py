import sys
sys.stdin = open("input68.txt", "rt")

def DFS(x, y):
    global cnt
    if x == y == 6:
        cnt += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 7 and 0 <= ny < 7 and board[ny][nx] == 0:
                board[ny][nx] = 1
                DFS(nx, ny)
                board[ny][nx] = 0

if __name__ == '__main__':
    board = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    board[0][0] = 1
    DFS(0, 0)
    print(cnt)