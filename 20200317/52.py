import sys
sys.stdin = open("input52.txt", "rt")

def DFS(L):
    global cnt
    if L == m:
        for i in range(L):
            print(res[i], end=' ')
        cnt += 1
        print()
    else:
        for j in range(1, n+1):
            if ch[j] == 0:
                ch[j] = 1
                res[L] = j
                DFS(L+1)
                ch[j] = 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    ch = [0] * (n + 1)
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)