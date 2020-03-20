import sys
sys.stdin = open("input58.txt", "rt")

def DFS(E):
    global cnt
    if E == n:
        cnt += 1
        for v in path:
            print(v, end=' ')
        print()
    else:
        for i in range(1, n+1):
            if g[E][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i] = 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    g = [[0]*(n+1) for _ in range(n+1)]
    ch = [0]*(n+1)
    for _ in range(m):
        p, q = map(int, input().split())
        g[p][q] = 1
    cnt = 0
    path = list()
    ch[1] = 1
    path.append(1)
    DFS(1)
    print(cnt)