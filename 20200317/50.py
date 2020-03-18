import sys
sys.stdin = open("input50.txt", "rt")

def DFS(L):
    global cnt
    if L == m:
        cnt += 1
        for v in a:
            print(v, end=' ')
        print()
    else:
        for i in range(1, n+1):
            a[L] = i
            DFS(L+1)

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)