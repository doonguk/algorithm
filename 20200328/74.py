import sys
from collections import deque
sys.stdin = open("input74.txt", "rt")

# 매 체크마다 board를 순회하며 0이 모두 1인지 체크하는건 n2 비효율 worst case  > 0.1초
# 1이 하나도 없는 case 생

if __name__ == '__main__':
    m, n = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    ch = [[0]*m for _ in range(n)]
    res = 0
    cnt = 0 # 바꿔야하는 감의 수
    dQ = deque()
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    for y in range(n):
        for x in range(m):
            if board[y][x] == 0:
                cnt += 1
            elif board[y][x] == 1:
                dQ.append((x,y))

    if cnt == 0:
        if len(dQ) == 0:
            print(-1) # 모두 빈 공간
        else:
            print(0) # 애초에 모두 1
    else:
        while cnt > 0 and dQ:
            for _ in range(len(dQ)):
                x, y = dQ.popleft()
                for i in range(4):
                    xx = x + dx[i]
                    yy = y + dy[i]
                    if 0 <= xx < m and 0 <= yy < n and ch[yy][xx] == 0 and board[yy][xx] == 0:
                        cnt -= 1
                        dQ.append((xx, yy))
                        ch[yy][xx] = 1
            res += 1
        if cnt > 0:
            print(-1)
        else:
            print(res)
