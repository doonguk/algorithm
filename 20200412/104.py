import sys
sys.stdin = open("input104.txt", "rt")


def DFS(L, s):
    global res
    if L == m:
        sum = 0
        for v in hs:
            x = v[0]
            y = v[1]
            dis = 2147000000
            for v2 in cb:
               x2 = pz[v2][0]
               y2 = pz[v2][1]
               dis = min(dis, abs(x - x2) + abs(y - y2))
            sum += dis
        if sum < res:
            res = sum
    else:
        for i in range(s, len(pz)):
            cb[L] = i
            DFS(L+1, i+1)

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    hs = list()
    pz = list()
    cb = [0] * m # 조합의 경우의 수
    res = 2147000000
    for y in range(n):
        for x in range(n):
            if board[y][x] == 2:
                pz.append((x,y))
            elif board[y][x] == 1:
                hs.append((x,y))

    DFS(0, 0)
    print(res)